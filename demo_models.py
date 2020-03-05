from app import app, db
from app.models import Person, Message


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Person': Person, 'Message': Message}
