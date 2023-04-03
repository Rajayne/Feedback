from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.Text(20), primary_key=True, 
                         unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text(50), unique=True, 
                      nullable=False)
    first_name = db.Column(db.Text(30), nullable=False)
    last_name = db.Column(db.Text(30), nullable=False)

    def __repr__(self):
        u = self
        return f'{u.username} {u.email} {u.first_name} {u.last_name}'