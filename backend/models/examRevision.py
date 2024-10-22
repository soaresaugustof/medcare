from . import db

class ExamRevision(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    diagnosis_id = db.Column(db.Integer, db.ForeignKey('diagnosis.id'))
    comments = db.Column(db.String(1000))
    revision_status = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, func.now())