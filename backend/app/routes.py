from flask import jsonify, request
import bcrypt
from .config import mydb  # Certifique-se de que mydb é gerenciado corretamente

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    try:
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        tipo_usuario = request.json['tipo_usuario']
        especialidade = request.json['especialidade']
        
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

        cursor = mydb.cursor()
        cursor.execute("""INSERT INTO Usuario (nome, email, senha, tipo_usuario, especialidade)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (nome, email, senha_hash.decode('utf-8'), tipo_usuario, especialidade))
        
        mydb.commit()
        cursor.close()
        return jsonify({'message': 'Usuário cadastrado com sucesso!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login_usuario():
    try:
        email = request.json['email']
        senha = request.json['senha']
        
        cursor = mydb.cursor()
        cursor.execute("SELECT idUsuario, nome, senha, tipo_usuario FROM Usuario WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()

        if not usuario:
            return jsonify({'message': 'Email ou senha incorretos'}), 401
        
        idUsuario, nome, senha_hash, tipo_usuario = usuario
        
        if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
            return jsonify({'message': f'Bem-vindo(a) {nome}!', 'tipo_usuario': tipo_usuario}), 200
        else:
            return jsonify({'message': 'Email ou senha incorretos'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM paciente")
        pacientes = cursor.fetchall()
        return jsonify(pacientes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
