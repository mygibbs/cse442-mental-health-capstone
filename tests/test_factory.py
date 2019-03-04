from app import create_app

from config import Config


class TestConfig(Config):
    TESTING = True


def test_config():
    assert not create_app().testing
    assert create_app(TestConfig).testing
