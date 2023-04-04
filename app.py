from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User
from forms import RegisterForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

app.config["SECRET_KEY"] = "key"

connect_db(app)
db.create_all()

@app.route('/', methods=['GET'])
def redirect():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.username.data
        password = form.password.data

        user = User.register(name, password)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            form.username.errors.append('Username taken.')
        
    else:
        return render_template('register.html', form=form)