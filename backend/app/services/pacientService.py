from app.models.pacient import Pacient
from app import db

class PacientService:
    
    @staticmethod
    def getPacientById(pacientId):
        return Pacient.query.get(pacientId)
    
    @staticmethod
    def getAllPacients():
        return Pacient.query.all()
    
    @staticmethod
    def createPacient(name, birthDate, cpf, email, phone, address, healthCarePlan):
        newPacient = Pacient(
            name           = name,
            birthDate      = birthDate,
            cpf            = cpf,
            email          = email,
            phone          = phone,
            address        = address,
            healthCarePlan = healthCarePlan
        )
        db.session.add(newPacient)
        db.session.commit()
        return newPacient
    
    @staticmethod
    def updatePacient(pacientId, **kwargs):
        pacient = Pacient.query.get(pacientId)
        if not pacient:
            return None
        
        for key, value in kwargs.items():
            setattr(pacient, key, value)
        
        db.session.commit()
        return pacient
    
    @staticmethod
    def deletePacient(pacientId):
        pacient = Pacient.query.get(pacientId)
        if pacient:
            db.session.delete(pacient)
            db.session.commit()
        return pacient
