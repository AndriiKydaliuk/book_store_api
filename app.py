"""Main application module"""
from typing import Optional
from pathlib import Path

import connexion

from flask import Flask, url_for, request, render_template
from flask_login import LoginManager, login_user, login_required

from config import get_environment_config
from database import db
from dependencies import ma
from models.user_model import User
from routes.home_route import home_control
from routes.login_route import login_control
from routes.user_route import user_control, user_manipulation
from routes.product_route import product_control, product_manipulation
from routes.store_item_route import store_item_control, store_item_manipulation
from routes.booking_route import booking_control, booking_manipulation
from authenticator import jwt_authentication


def create_app() -> Flask:
    """Factory method for Flask provider."""
    options = {'swagger_ui': True}
    connexion_app = connexion.App("__name__",
                                  specification_dir=str(Path(__file__).parent) + './openapi/',
                                  options=options)
    connexion_app.add_api('swagger.yml')
    application = connexion_app.app
    # Configuring from Python module
    application.config.from_object(get_environment_config())
    # Initializing the database
    db.init_app(application)
    # Initializing the marshmallow extension
    ma.init_app(application)

    # Context manager to make it possible to access application object outside the module
    with application.app_context():
        db.create_all()
        return application


def add_routes(application):
    """Add routes for user management purposes."""
    # application.add_url_rule("/", methods=["GET"], view_func=home_control)

    application.add_url_rule("/login", methods=["GET"], view_func=login_control)

    application.add_url_rule("/user", methods=["GET", "POST"], view_func=user_control)
    application.add_url_rule('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'], view_func=user_manipulation)

    application.add_url_rule("/product", methods=["GET", "POST"], view_func=product_control)
    application.add_url_rule('/product/<int:product_id>', methods=['GET', 'PUT', 'DELETE'],
                             view_func=product_manipulation)

    application.add_url_rule("/store_item", methods=["GET", "POST"], view_func=store_item_control)
    application.add_url_rule('/store_item/<int:store_item_id>', methods=['GET', 'PUT', 'DELETE'],
                             view_func=store_item_manipulation)

    application.add_url_rule("/booking", methods=["GET", "POST"], view_func=booking_control)
    application.add_url_rule('/booking/<int:booking_id>', methods=['GET', 'PUT', 'DELETE'],
                             view_func=booking_manipulation)


def initialize_login_manager(application: Flask) -> LoginManager:
    """Initialize Flask-login manager for the application."""
    manager = LoginManager()
    manager.login_view = 'login'
    manager.init_app(application)
    return manager


app = create_app()
login_manager = initialize_login_manager(app)
app.create_jinja_environment()


@login_manager.user_loader
def load_login_user(token: str) -> Optional[User]:
    """Loads user based on the JWT token information."""
    jwt_token = jwt_authentication(token)
    if jwt_token:
        model_id = jwt_token.get('sub')
        return User.query.get(int(model_id))
    return None


@app.route('/catalogue')
@login_required
def catalogue():
    """Default route for home page"""
    from services.product_service import ProductService
    products = ProductService.get_all()
    return render_template('catalogue.html', products=products, title='Catalogue')


@app.route('/users')
@login_required
def users_page():
    """Route for users page"""
    from services.user_service import UserService
    users = UserService.get_all()
    return render_template('users.html', users=users, title='Users')


@app.route('/login', methods=['POST'])
def login_post():
    """Route for the POST request to the login endpoint."""
    bearer = request.headers.get('Authorization')  # Bearer YourTokenHere
    token = bearer.split()[1]
    user = load_login_user(token)
    if user:
        login_user(user, remember=True)
        return url_for('catalogue')
    error = "Please try again"
    return render_template('login.html', error=error)


if __name__ == "__main__":
    """Entry point."""
    # add routes for the created application
    add_routes(app)
    app.run()
