"""
conftest for test direcrory
"""
import pytest
from app import create_app, add_routes


@pytest.fixture()
def app():
    app = create_app()
    add_routes(app)
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
