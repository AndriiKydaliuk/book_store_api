"""Module with tools for authentication"""
from typing import Optional
from werkzeug.exceptions import Unauthorized
from flask_httpauth import HTTPBasicAuth

from models.user_model import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(login, password):
    # Checks login/password pair for authentication
    user = User.query.filter_by(login=login).first()
    if not user or not user.verify_password(password):
        return False
    return True


def jwt_authentication(token: str) -> Optional[dict]:
    """Used by swagger for JWT authentication."""
    try:
        return User.decode_token(token)
    except Unauthorized:
        return None


def basic_authentication(username: str, password: str) -> Optional[dict]:
    """Used by swagger for Basic authentication."""
    user = User.query.filter_by(login=username).first()
    if user and user.verify_password(password):
        return {"sub": username}
    return None

