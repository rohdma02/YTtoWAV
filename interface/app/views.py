from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/tracks')
def tracks():
    return render_template('tracks.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/logout')
def logout():
    return render_template('logout.html')


@main.route('/register')
def register():
    return render_template('register.html')
