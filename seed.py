from models import db, connect_db, User
from app import app

db.drop_all()
db.create_all()

