"""Login routes module."""
from flask import request

from controllers.login_controller import LoginController


def login_control():
    """URL to collect information about users or create new one."""
    if request.method == 'GET':
        return LoginController.get()
