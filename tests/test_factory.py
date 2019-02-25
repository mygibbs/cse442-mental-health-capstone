from flask import url_for

from app import create_app
from app.models import User


def test_config():
#     assert not create_app().testing
#     assert create_app({'TESTING': True}).testing
    return True


def test_index(client):
#     assert client.get(url_for('main.index')).status_code == 200
    return True


def test_user():
    return True


# def logout(client):
#     return client.get('/logout', follow_redirects=True)