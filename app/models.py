from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(64), index=True)
    projects = db.relationship('Project', backref='student', lazy='dynamic')
    advisor_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))

    def __repr__(self):
        return "<student_name {}, advisor_id {}>".format(self.student_name, self.advisor_id)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(64), index=True)
    advisees = db.relationship('Student', backref='advisor', lazy='dynamic')

    def __repr__(self):
        return "<teacher_name {}>".format(self.teacher_name)

class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exhibition_name = db.Column(db.String(64), index=True, unique=True)
    template_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __repr__(self):
        return "<exhibition_name {}, template_id {}".format(self.exhibition_name, self.template_id)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    exhibition_id = db.Column(db.Integer, db.ForeignKey('exhibition.id'))
    title = db.Column(db.String(64), index=True) # title assigned by student
    stages = db.relationship('Stage', backref='project', lazy='dynamic')
    completetion_status = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return "<title {}, student_id {}, exhibition_id {}, completion_status {}".format(self.title, self.student_id, self.exhibition_id, self.completion_status)

class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    timestamp = db.Column(db.DateTime, index=True)
    signer_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    checked = db.Column(db.Boolean, index=True)
    order = db.Column(db.Integer)

    def __repr__(self):
        return "<name {}, checked {}, timestamp {}, order {}, project_id {}, signer_id {}".format(self.name, self.checked, self.timestamp, self.order, self.project_id, self.signer_id)
