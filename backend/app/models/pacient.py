from . import db

class Pacient(db.Model):
    __tablename__ = "pacient"
    
    id              = db.Column(db.Integer, primary_key = True)
    name            = db.Column(db.String(100), nullable = False)
    birthDate       = db.Column(db.String(10))
    cpf             = db.Column(db.String(11))
    email           = db.Column(db.String(100), nullable = False)
    phone           = db.Column(db.String(11), nullable = False)
    address         = db.Column(db.String(100))
    healthCarePlan  = db.Column(db.String(4))
    createdAt       = db.Column(db.DateTime, func.now())
    lastUpdate      = db.Column(db.DateTime)