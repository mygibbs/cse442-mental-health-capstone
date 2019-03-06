from app.models import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase:
    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


def test_register(client):
    response = client.get('/register', follow_redirects=True)
    assert response.status_code == 200

    response = client.post(
        '/register', data={'username': 'a', 'password': 'a', 'email': 'a'}, follow_redirects=True
    )
    assert response.status_code == 200


def test_login(client):
    response = client.get('/login', follow_redirects=True)
    assert response.status_code == 200


def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200


def test_achievements(client):
    response = client.get('/achievements', follow_redirects=True)
    assert response.status_code == 200


def test_progress(client):
    response = client.get('/progress', follow_redirects=True)
    assert response.status_code == 200


def test_profile(client):
    response = client.get('/profile', follow_redirects=True)
    assert response.status_code == 200

