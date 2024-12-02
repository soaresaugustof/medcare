import bcrypt
from flask import jsonify, request
from backend import app
from .config import mydb  # Certifique-se de que mydb é gerenciado corretamente
from app.services.userService import UserService
from app.services.pacientService import PacientService
from app.services.examService import ExamService
from app.services.examRevisionService import ExamRevisionService
from app.services.diagnosisService import DiagnosisService

#----------ROTAS DE USUÁRIO

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


#----------ROTAS DE PACIENTE

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
    

@app.route('/pacientes/<int:pacient_id>', methods=['GET'])
def get_pacient_by_id(pacient_id):
    try:
        pacient = PacientService.getPacientById(pacient_id)
        if not pacient:
            return jsonify({'message': 'Pacient not found'}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pacientes', methods=['POST'])
def create_pacient():
    try:  
        data = request.json
        pacient = PacientService.createPacient(**data)
        return jsonify(pacient.to_dict()), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pacientes/<int:pacient_id>', methods=['PUT'])
def update_pacient(pacient_id):
    try:
        data = request.json
        pacient = PacientService.updatePacient(pacient_id, **data)
        if not pacient:
            return jsonify({'message': 'Pacient not found'}), 404
        
        return jsonify(pacient.to_dict())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pacientes/<int:pacient_id>', methods=['DELETE'])
def delete_pacient(pacient_id):
    try:
        pacient = PacientService.deletePacient(pacient_id)
        if not pacient:
            return jsonify({'message': 'Pacient not found'}), 404
        
        return jsonify({'message': 'Pacient deleted successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#----------ROTAS DE EXAME


@app.route('/exames', methods=['GET'])
def get_all_exams():
    try:
        exams = ExamService.getAllExams()
        return jsonify([exam.to_dict() for exam in exams])

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/exames/<int:exam_id>', methods=['GET'])
def get_exam_by_id(exam_id):
    try:
        exam = ExamService.getExamById(exam_id)
        if not exam:
            return jsonify({'message': 'Exam not found'}), 404
        return jsonify(exam.to_dict())

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/exames', methods=['POST'])
def create_exam():
    try:
        data = request.json
        exam = ExamService.createExam(**data)
        return jsonify(exam.to_dict()), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/exames/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    try:
        data = request.json
        exam = ExamService.updateExam(exam_id, **data)
        if not exam:
            return jsonify({'message': 'Exam not found'}), 404
        return jsonify(exam.to_dict())

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/exames/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    try:
        exam = ExamService.deleteExam(exam_id)
        if not exam:
            return jsonify({'message': 'Exam not found'}), 404
        return jsonify({'message': 'Exam deleted successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


#----------ROTAS DE DIAGNÓSTICO


@app.route('/diagnosis', methods=['GET'])
def get_all_diagnoses():
    try:        
        diagnoses = DiagnosisService.getAllDiagnoses()
        return jsonify([diagnosis.to_dict() for diagnosis in diagnoses])

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/diagnosis/<int:diagnosis_id>', methods=['GET'])
def get_diagnosis_by_id(diagnosis_id):
    try:
        diagnosis = DiagnosisService.getDiagnosisById(diagnosis_id)
        if not diagnosis:
            return jsonify({'message': 'Diagnosis not found'}), 404
        
        return jsonify(diagnosis.to_dict())

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/diagnosis', methods=['POST'])
def create_diagnosis():
    try:
        data = request.json
        diagnosis = DiagnosisService.createDiagnosis(**data)
        
        return jsonify(diagnosis.to_dict()), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/diagnosis/<int:diagnosis_id>', methods=['PUT'])
def update_diagnosis(diagnosis_id):
    try:
        data = request.json
        diagnosis = DiagnosisService.updateDiagnosis(diagnosis_id, **data)
        if not diagnosis:
            return jsonify({'message': 'Diagnosis not found'}), 404
        
        return jsonify(diagnosis.to_dict())

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/diagnosis/<int:diagnosis_id>', methods=['DELETE'])
def delete_diagnosis(diagnosis_id):
    try:
        diagnosis = DiagnosisService.deleteDiagnosis(diagnosis_id)
        if not diagnosis:
            return jsonify({'message': 'Diagnosis not found'}), 404
    
        return jsonify({'message': 'Diagnosis deleted successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#----------ROTAS DE REVISÃO DE EXAME


@app.route('/exam_revisions', methods=['GET'])
def get_all_exam_revisions():
    try:
        revisions = ExamRevisionService.getAllExamRevisions()
        return jsonify([revision.to_dict() for revision in revisions])

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/exam_revisions/<int:revision_id>', methods=['GET'])
def get_exam_revision_by_id(revision_id):
    try:
        revision = ExamRevisionService.getExamRevisionById(revision_id)
        if not revision:
            return jsonify({'message': 'Exam Revision not found'}), 404
    
        return jsonify(revision.to_dict())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/exam_revisions', methods=['POST'])
def create_exam_revision():
    try:
        data = request.json
        revision = ExamRevisionService.createExamRevision(**data)
        
        return jsonify(revision.to_dict()), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/exam_revisions/<int:revision_id>', methods=['PUT'])
def update_exam_revision(revision_id):
    try:
        data = request.json
        revision = ExamRevisionService.updateExamRevision(revision_id, **data)
        if not revision:
            return jsonify({'message': 'Exam Revision not found'}), 404
    
        return jsonify(revision.to_dict())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/exam_revisions/<int:revision_id>', methods=['DELETE'])
def delete_exam_revision(revision_id):
    try:
        revision = ExamRevisionService.deleteExamRevision(revision_id)
        if not revision:
            return jsonify({'message': 'Exam Revision not found'}), 404
    
        return jsonify({'message': 'Exam Revision deleted successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500