"""
conftest for test direcrory
"""
import pytest
from app import create_app, add_routes
from selenium import webdriver


@pytest.fixture()
def app():
    app = create_app()
    add_routes(app)
    # app.config.update({
    #     "TESTING": True,
    # })
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
