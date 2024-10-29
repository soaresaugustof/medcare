from . import db

class Diagnosis(db.Model):
    __tablename__ = "diagnosis"
    
    id          = db.Column(db.Integer, primary_key = True)
    examId      = db.Column(db.Integer, db.ForeignKey('exam.id'))
    examFile    = db.Column(db.String(1000))
    result      = db.Column(db.String(1000))
    probability = db.Column(Numeric(precision = 10, scale = 2))
    createdAt   = db.Column(db.DateTime, func.now())