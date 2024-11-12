from app.models.exam import Exam
from app import db

class ExamService:
    
    @staticmethod
    def getExamById(examId):
        return Exam.query.get(examId)
    
    @staticmethod
    def getAllExams():
        return Exam.query.all()
    
    @staticmethod
    def createExam(pacientId, birthDate, examFile, userId):
        newExam = Exam(
            pacientId = pacientId,
            birthDate = birthDate,
            examFile  = examFile,
            userId    = userId
        )
        db.session.add(newExam)
        db.session.commit()
        return newExam
    
    @staticmethod
    def updateExam(examId, **kwargs):
        exam = Exam.query.get(examId)
        if not exam:
            return None
        
        for key, value in kwargs.items():
            setattr(exam, key, value)
        
        db.session.commit()
        return exam
    
    @staticmethod
    def deleteExam(examId):
        exam = Exam.query.get(examId)
        if exam:
            db.session.delete(exam)
            db.session.commit()
        return exam
