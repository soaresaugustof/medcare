from app.models.exam_revision import ExamRevision
from app import db

class ExamRevisionService:
    
    @staticmethod
    def getRevisionById(revisionId):
        return ExamRevision.query.get(revisionId)
    
    @staticmethod
    def getAllRevisions():
        return ExamRevision.query.all()
    
    @staticmethod
    def createRevision(diagnosisId, comments, revisionStatus, userId):
        newRevision = ExamRevision(
            diagnosisId    = diagnosisId,
            comments       = comments,
            revisionStatus = revisionStatus,
            userId         = userId
        )
        db.session.add(newRevision)
        db.session.commit()
        return newRevision
    
    @staticmethod
    def updateRevision(revisionId, **kwargs):
        revision = ExamRevision.query.get(revisionId)
        if not revision:
            return None
        
        for key, value in kwargs.items():
            setattr(revision, key, value)
        
        db.session.commit()
        return revision
    
    @staticmethod
    def deleteRevision(revisionId):
        revision = ExamRevision.query.get(revisionId)
        if revision:
            db.session.delete(revision)
            db.session.commit()
        return revision
