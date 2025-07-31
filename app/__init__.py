from flask import Flask
from flask_login import LoginManager
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .database import init_db

    init_db(app)

    # --- Flask-Login Configuration ---
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.login_message = "Silakan login untuk mengakses halaman ini."

    # Import User model here to avoid circular imports
    from .database.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        """Function for Flask-Login to reload the user object from the user ID stored in the session."""
        return User.query.get(int(user_id))

    from .routes import register_blueprints

    register_blueprints(app)

    return app
