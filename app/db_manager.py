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

def create_student(name, advisor_name):
	"""
	Creates a student and relates it to a teacher via advisor_name
	Takes two strings as name and advisor_name
	"""
	s = Student()
	s.student_name = name
	# sqlalchemy.orm.exc.NoResultFound error will be thrown if teacher not found
	s.advisor_id = Teacher.query.filter_by(teacher_name=teacher_name).one()
