"""Flask application configuration."""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configuration class."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "gym-management-secret-key-change-in-production")

    # Use DATABASE_URL env var if set (e.g. MySQL), otherwise default to SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(basedir, "gym.db"),
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
