"""Module to manage ORM Customer model."""

import enum
import hashlib
import os
import time

import jwt

from flask_login import UserMixin
from werkzeug.exceptions import Unauthorized

from database import db


class Role(enum.Enum):
    ADMIN = 1
    MANAGER = 2
    CUSTOMER = 3


class User(UserMixin, db.Model):
    """User table specification."""

    JWT_LIFETIME_SECONDS = 600
    JWT_ALGORITHM = "HS256"

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    login = db.Column(db.String(256), unique=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    booking = db.relationship('Booking', backref='users', lazy=True)
    token = None

    def __repr__(self) -> str:
        return f"<User {self.login}>"

    def hash_password(self, password: str):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        self.password_hash = salt + key

    def verify_password(self, password: str):
        salt, key = self.password_hash[:32], self.password_hash[32:]
        new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return key == new_key

    @staticmethod
    def _current_timestamp() -> int:
        """Gets current timestamp."""
        return int(time.time())

    def generate_token(self) -> str:
        """Generates JWT token."""
        timestamp = self._current_timestamp()
        payload = {
            "iat": int(timestamp),
            "exp": int(timestamp + self.JWT_LIFETIME_SECONDS),
            "sub": str(self.id),
        }
        self.token = jwt.encode(payload, 'SECRET_KEY', algorithm=self.JWT_ALGORITHM)

        return self.token

    @classmethod
    def decode_token(cls, token):
        """Decodes data from JWT token."""
        try:
            return jwt.decode(token, 'SECRET_KEY', algorithms=[cls.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise Unauthorized('Invalid token. Please log in again.')
        except TypeError:
            raise Unauthorized('Invalid token. Please log in again.')

    def get_id(self):
        """Get user Id for Login Manager."""
        if self.token:
            try:
                self.decode_token(self.token)
            except Unauthorized:
                self.generate_token()
        else:
            self.generate_token()
        return self.token

