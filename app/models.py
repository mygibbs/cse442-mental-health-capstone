import base64
from datetime import datetime, timedelta
import os

from flask import url_for

from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class User(PaginatedAPIMixin, UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    points = db.Column(db.Integer, default=0)
    lastlogin = db.Column(db.Integer)#this will be in ticks(seconds)
    currstreak = db.Column(db.Integer)#min value = 1
    multiplier = db.Column(db.Float)#multiplier float in the range of [1, 3]
    achievement1 = db.Column(db.Integer, default=0)
    achievement2 = db.Column(db.Integer, default=0)
    achievement3 = db.Column(db.Integer, default=0)
    achievement4 = db.Column(db.Integer, default=0)
    achievement5 = db.Column(db.Integer, default=0)
    achievement6 = db.Column(db.Integer, default=0)
    achievement7 = db.Column(db.Integer, default=0)
    achievement8 = db.Column(db.Integer, default=0)
    achievement9 = db.Column(db.Integer, default=0)
    achievement10 = db.Column(db.Integer, default=0)
    quiz_taken = db.Column(db.Integer, default=0)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'password_hash': self.password_hash,
            'points': self.points,
            'lastlogin': self.lastlogin,
            'currstreak': self.currstreak,
            'multiplier': self.multiplier,
            'achievement1': self.achievement1,
            'achievement2': self.achievement2,
            'achievement3': self.achievement3,
            'achievement4': self.achievement4,
            'achievement5': self.achievement5,
            'achievement6': self.achievement6,
            'achievement7': self.achievement7,
            'achievement8': self.achievement8,
            'achievement9': self.achievement9,
            'achievement10': self.achievement10
        }
        if include_email:
            data['email'] = self.email
        return data

    # TODO: modify fields
    def from_dict(self, data, new_user=False):
        for field in ['username', 'email']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + datetime.timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + datetime.timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - datetime.timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except:
        return None
