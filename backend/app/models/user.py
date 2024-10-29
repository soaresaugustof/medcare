from . import db

class User(db.Model):
    __tablename__ = "user"
    
    id          = db.Column(db.Integer, primary_key = True)
    name        = db.Column(db.String(100), nullable = False)
    email       = db.Column(db.String(100), nullable = False)
    password    = db.Column(db.String(150), nullable = False)
    userType    = db.Column(db.String(2))
    speciality  = db.Column(db.String(30))
    createdAt   = db.Column(db.DateTime, func.now())
    lastUpdate  = db.Column(db.DateTime)