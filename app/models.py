from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(64), index=True)
    projects = db.relationship('Project', backref='student', lazy='dynamic')
    advisor_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    def __repr__(self):
        pass

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(64), index=True)
    advisees = db.relationship('Student', backref='advisor', lazy='dynamic')

    def __repr__(self):
        pass

class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exhibition_name = db.Column(db.String(64), index=True, unique=True)
    template_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        pass

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    exhibition_id = db.Column(db.Integer, db.ForeignKey('exhibition.id'))
    title = db.Column(db.String(64), index=True) # title assigned by student
    stages = db.relationship('Stage', backref='project', lazy='dynamic')
    completetion_status = db.Column(db.Boolean, index=True)

    def __repr__(self):
        pass

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    timestamp = db.Column(db.DateTime, index=True)
    signer_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    checked = db.Column(db.Boolean, index=True)
    order = db.Column(db.Integer)

    def __repr__(self):
        pass
