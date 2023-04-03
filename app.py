from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db
# from forms import 
from sqlalchemy.exc import IntegrityError

app = Flask(__name__,template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

app.config["SECRET_KEY"] = "key"

connect_db(app)
db.create_all()