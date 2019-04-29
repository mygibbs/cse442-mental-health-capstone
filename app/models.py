from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer)
    lastlogin = db.Column(db.Integer)#this will be in ticks(seconds)
    currstreak = db.Column(db.Integer)#min value = 1
    achievement1 = db.Column(db.Integer)
    achievement2 = db.Column(db.Integer)
    achievement3 = db.Column(db.Integer)
    achievement4 = db.Column(db.Integer)
    achievement5 = db.Column(db.Integer)
    achievement6 = db.Column(db.Integer)
    achievement7 = db.Column(db.Integer)
    achievement8 = db.Column(db.Integer)
    achievement9 = db.Column(db.Integer)
    achievement10 = db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
