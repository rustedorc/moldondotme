
"""
This module contains the SQLAlchemy and Flask-Login extensions for the MoldonDotMe application.

The `db` object is an instance of the `SQLAlchemy` class, which provides an interface
to interact with the database.

The `login_manager` object is an instance of the `LoginManager` class, which provides
user authentication and session management functionality.

Usage:
    To use the `db` and `login_manager` objects, simply import them from this module
    and use them in your Flask application:

    ```python
    from extensions import db, login_manager

    # Example usage
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
    ```
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
