from flask import Flask


def create_app():
    app = Flask(__name__)

    # Import the models module
    from app.views import main
    app.register_blueprint(main)

    return app
