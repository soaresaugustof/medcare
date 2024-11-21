import bcrypt
from flask import jsonify, request
from backend import app
from ..config import mydb  # Certifique-se de que mydb é gerenciado corretamente
from app.services.userService import UserService

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    try:
        #Criação de parâmetros
        name       = request.json['nome']
        email      = request.json['email']
        password   = request.json['senha']
        userType   = request.json['tipo_usuario']
        speciality = request.json['especialidade']
        
        salt       = bcrypt.gensalt()
        hashPass   = bcrypt.hashpw(password.encode('utf-8'), salt)

        user = UserService.createUser(
            name       = name,
            email      = email,
            password   = hashPass,
            userType   = userType,
            speciality = speciality
        )
        
        #cursor = mydb.cursor()
        #cursor.execute("""INSERT INTO Usuario (nome, email, senha, tipo_usuario, especialidade)
        #                  VALUES (%s, %s, %s, %s, %s)""",
        #               (nome, email, senha_hash.decode('utf-8'), tipo_usuario, especialidade))
        
        #mydb.commit()
        #cursor.close()
        return jsonify({'message': 'Usuário ' + user.name + ' cadastrado com sucesso!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login_usuario():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('senha')

        if not email or not password:
            return jsonify({'message': 'Email e senha são obrigatórios'}), 400

        user = UserService.authenticate(email, password)
        
        if not user:
            return jsonify({'message': 'Email ou senha incorretos'}), 401
        
        return jsonify({
            'message': f'Bem-vindo(a) {user.name}!',
            'tipo_usuario': user.user_type
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        users = UserService.getAllUsers()
        return jsonify(users)
        #cursor = mydb.cursor()
        #cursor.execute("SELECT * FROM paciente")
        #pacientes = cursor.fetchall()
        #return jsonify(pacientes)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500