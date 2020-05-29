from app import db
from app.models import Student, Teacher, Exhibition, Project, Stage

def create_teacher(name):
	"""
	Creates a teacher and commits it to db
	Takes a string as name
	"""
	t = Teacher()
	t.teacher_name = name
	db.session.add(t)
	db.session.commit()
