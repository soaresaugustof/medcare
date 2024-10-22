from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    senha = db.Column(db.String(150), nullable = False)
    user_type = db.Column(db.String(2))
    speciality = db.Column(db.String(30))
    created_at = db.Column(db.DateTime, func.now())
    last_update = db.Column(db.DateTime)