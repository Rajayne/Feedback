from models import db, connect_db, User
from app import app

db.drop_all()
db.create_all()

user = User.register('AbominableSnow', 'password', 'abom123@email.com', 'Abi', 'Noble')
db.session.add(user)
db.session.commit()