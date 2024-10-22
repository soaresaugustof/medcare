from . import db

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pacient_id = db.Column(db.Integer, db.ForeignKey('pacient.id'))
    birth_date = db.Column(db.String(10))
    exam_file = db.Column(db.LargeBinary)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, func.now())
    last_update = db.Column(db.DateTime)