from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from forms import RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__,template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.app_context().push()

app.config["SECRET_KEY"] = "key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/', methods=['GET'])
def home():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User.register(username, password, email, first_name, last_name)
        db.session.add(user)
        try:
            db.session.commit()
            return redirect('/secret')
        except IntegrityError:
            db.session.rollback()
            form.username.errors.append('Username taken.')
            return render_template('register.html', form=form)
    else:
        return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            flash(f'Welcome back, {user.username}!')
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else: form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)

@app.route('/users/<username>', methods=['GET'])
def user_page(username):
    if 'username' not in session:
        flash('You must be logged in to view!')
        return redirect('/login')
    else:
        if session['username'] == username:
            user = User.query.get_or_404(username)
            posts = user.posts   
            return render_template('users.html', user=user, posts=posts)
        else:
            user = User.query.get_or_404(session['username'])
            flash(f"You do not have access to this page!")
            return redirect(f'/users/{user.username}')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username')
    flash('Goodbye!')
    return redirect('/login')