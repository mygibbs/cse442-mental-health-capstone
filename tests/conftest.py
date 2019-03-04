import pytest

from app import create_app

from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


@pytest.fixture
def app():

    app = create_app(TestConfig)

    with app.app_context():
        app.init_db()
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
