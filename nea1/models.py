from nea import db
db.create_all()
from nea import User, Lead
user_1=User(username="nyanya", email="a@demo.com", password="password")
db.session.add(user_1)
