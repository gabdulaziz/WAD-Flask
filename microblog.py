from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'sa': __import__('sqlalchemy'), 'so': __import__('sqlalchemy.orm'),
            'db': db, 'User': User, 'Post': Post}