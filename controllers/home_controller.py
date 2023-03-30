"""HomeController module."""
from flask import render_template
from flask_login import login_required


class HomeController:
    """Class to communicate directly with the services."""

    @staticmethod
    @login_required
    def get():
        """Default route for home page"""
        from services.user_service import UserService
        users = UserService.get_all()
        return render_template('users.html', users=users, title='Main Page')

