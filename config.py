"""Module to store environment configs"""

import os


class Config(object):
    """Parent class for environment configs"""

    ENV = os.environ["ENV"] if "ENV" in os.environ else "DEVELOPMENT"
    CSRF_ENABLED = True
    SECRET_KEY = "this_is_a_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development environment config"""

    DEBUG = True
    # will be searching for dev.db file in instance folder, if does not exist, will create new one
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class TestingConfig(Config):
    """Test environment config"""

    DEBUG = False
    # will be searching for test.db file in instance folder, if does not exist, will create new one
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"


def get_environment_config() -> str:
    """To supports several environments"""

    if Config.ENV == "TESTING":
        return "config.TestingConfig"
    elif Config.ENV == "DEVELOPMENT":
        return "config.DevelopmentConfig"
