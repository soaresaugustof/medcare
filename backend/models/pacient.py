from . import db

class Pacient(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    birth_date = db.Column(db.String(10))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(11), nullable = False)
    address = db.Column(db.String(100))
    health_care_plan = db.Column(db.String(4))
    created_at = db.Column(db.DateTime, func.now())
    last_update = db.Column(db.DateTime)