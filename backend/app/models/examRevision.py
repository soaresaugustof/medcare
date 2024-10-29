from . import db

class ExamRevision(db.Model):
    __tablename__ = "exam_revision"
    
    id              = db.Column(db.Integer, primary_key = True)
    diagnosisId     = db.Column(db.Integer, db.ForeignKey('diagnosis.id'))
    comments        = db.Column(db.String(1000))
    revisionStatus  = db.Column(db.String(1000))
    userId          = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdAt       = db.Column(db.DateTime, func.now())