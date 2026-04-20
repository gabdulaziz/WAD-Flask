from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Yude'}
    posts = [
        {
            'author': {'username': 'Shabiri'},
            'body': 'Tuma hela Tanzania'
        },
        {
            'author': {'username': 'Islam'},
            'body': 'hela imefika salama salmini'
        }
    ]
    return render_template('index.html', title='Homepage', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)