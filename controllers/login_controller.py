"""Login Controller module."""

from flask import render_template


class LoginController:
    """Class to communicate directly with the services."""

    @staticmethod
    def get():
        """GET login page"""
        return render_template('login.html')
