"""Main Flask application entry point for Gym Management System."""

import os
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from models import db, User
from config import Config


def create_app(config_class=Config):
    """Application factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    CSRFProtect(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register routes
    from routes import register_routes
    register_routes(app)

    # Create tables & seed default admin
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username="admin").first():
            admin = User(username="admin", email="admin@gym.com", role="admin")
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
            print("✔ Default admin user created (admin / admin123)")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
