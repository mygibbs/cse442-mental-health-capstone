from app.models import User
from config import Config
import pytest, flask


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase:
    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


def test_register(app, client):
    response = client.get('/register', follow_redirects=True)
    assert response.status_code == 200


def test_login(app, client):
    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200


def test_logout(app, client):
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


def test_achievements(app, client):
    response = client.get('/achievements', follow_redirects=True)
    assert response.status_code == 200


def test_progress(app, client):
    response = client.get('/progress', follow_redirects=True)
    assert response.status_code == 200


def test_profile(app, client):
    response = client.get('/profile', follow_redirects=True)
    assert response.status_code == 200


def test_index(app, client):
    @app.route('/')
    def index():
        return flask.request.method

