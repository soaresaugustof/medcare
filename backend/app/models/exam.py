from . import db

class Exam(db.Model):
    __tablename__ = "exam"
    
    id          = db.Column(db.Integer, primary_key = True)
    pacientId   = db.Column(db.Integer, db.ForeignKey('pacient.id'))
    birthDate   = db.Column(db.String(10))
    examFile    = db.Column(db.LargeBinary)
    userId      = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdAt   = db.Column(db.DateTime, func.now())
    lastUpdate  = db.Column(db.DateTime)