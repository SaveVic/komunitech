from flask import Flask


def register_blueprints(app: Flask):
    from .main import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
