from app import app, db
from app.models import Student, Teacher, Exhibition, Project, Stage


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Student': Student, 'Teacher': Teacher, 'Exhibition': Exhibition, 'Project': Project, 'Stage': Stage,}
