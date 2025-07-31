from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the SQLAlchemy instance
db = SQLAlchemy()
migrate = Migrate()


def init_db(app: Flask):
    """
    Initializes the database and creates tables if they don't exist.
    """
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()
