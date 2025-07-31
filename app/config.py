# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
load_dotenv()


class Config:
    """
    Base configuration class. Contains default configuration settings
    and settings loaded from environment variables.
    """

    # Secret key for signing cookies and other security-related needs
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "instance", "komunitech.db")
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
