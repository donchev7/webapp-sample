from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    middleware(app)
    route(app)
 
    return app

def middleware(app):
    """
    Register 0 or more middleware (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Swap request.remote_addr with the real IP address even if behind a proxy.
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return None

def route(app):
    """
    Add some routes to our test web app
    
    :param app: Flask application instance
    :return: Flask app
    """
    @app.route('/')
    @app.route('/index')
    @app.route('/home')
    def index():
        return "Hello bb beautiful world!"

    return app
