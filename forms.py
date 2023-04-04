from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import InputRequired, URL

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email =  StringField("Email", validators=[InputRequired(), URL()])
    first_name =  StringField("First Name", validators=[InputRequired()])
    last_name =  StringField("Last Name", validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    content = TextField("Content", validators=[InputRequired()])