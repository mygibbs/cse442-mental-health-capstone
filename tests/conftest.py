import pytest

from app import create_app, db
from app.models import User
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        u = User(username="test", email="test@example.com")
        u.set_password('test')
        db.session.add(u)
        db.session.commit()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
