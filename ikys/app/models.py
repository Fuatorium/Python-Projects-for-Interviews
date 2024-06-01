from . import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    performance_score = db.Column(db.Float, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position,
            'salary': self.salary,
            'performance_score': self.performance_score
        }

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position_applied = db.Column(db.String(100), nullable=False)
    interview_date = db.Column(db.DateTime, nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'position_applied': self.position_applied,
            'interview_date': self.interview_date
        }
