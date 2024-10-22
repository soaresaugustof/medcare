from . import db

class Diagnosis(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam_file = db.Column(db.String(1000))
    result = db.Column(db.String(1000))
    probability = db.Column(Numeric(precision = 10, scale = 2))
    created_at = db.Column(db.DateTime, func.now())