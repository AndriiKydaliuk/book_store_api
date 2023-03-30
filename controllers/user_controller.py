"""User Controller module."""

from authenticator import auth
from flask_login import login_required
from services.user_service import UserService


class UserController:
    """Class to communicate directly with the services."""

    @staticmethod
    def get(user_id: int):
        """Get user resource."""
        return UserService.get(user_id)

    @staticmethod
    def get_all():
        """Get all user resources."""
        return UserService.get_all()

    @staticmethod
    def create():
        """Create user resource."""
        return UserService.create()

    @staticmethod
    def delete(user_id: int):
        """Delete user resource."""
        return UserService.delete(user_id)

    @staticmethod
    def update(user_id: int):
        """Update user resource."""
        return UserService.update(user_id)
