"""Home Controller module."""
from flask import request

from controllers.home_controller import HomeController


def home_control():
    """URL to collect information about users or create new one."""
    if request.method == 'GET':
        return HomeController.get()

