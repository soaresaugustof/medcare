from app.models.diagnosis import Diagnosis
from app import db

class DiagnosisService:
    
    @staticmethod
    def getDiagnosisById(diagnosisId):
        return Diagnosis.query.get(diagnosisId)
    
    @staticmethod
    def getAllDiagnoses():
        return Diagnosis.query.all()
    
    @staticmethod
    def createDiagnosis(examId, examFile, result, probability):
        newDiagnosis = Diagnosis(
            examId      = examId,
            examFile    = examFile,
            result      = result,
            probability = probability
        )
        db.session.add(newDiagnosis)
        db.session.commit()
        return newDiagnosis
    
    @staticmethod
    def updateDiagnosis(diagnosisId, **kwargs):
        diagnosis = Diagnosis.query.get(diagnosisId)
        if not diagnosis:
            return None
        
        for key, value in kwargs.items():
            setattr(diagnosis, key, value)
        
        db.session.commit()
        return diagnosis
    
    @staticmethod
    def deleteDiagnosis(diagnosisId):
        diagnosis = Diagnosis.query.get(diagnosisId)
        if diagnosis:
            db.session.delete(diagnosis)
            db.session.commit()
        return diagnosis
