from flask import Flask
from .api.products_api import products_blueprint

# Create Flask instance and register products_blueprint.
def create_app():
    application = Flask(__name__)
    application.register_blueprint(products_blueprint)
    return application

# `app` holds the Flask instance for use outside this file, e.g., in `wsgi.py`.
app = create_app()