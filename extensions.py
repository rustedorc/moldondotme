
"""
This module contains the SQLAlchemy extension for the MoldonDotMe application.

The `db` object is an instance of the `SQLAlchemy` class, which provides an interface
to interact with the database.

Usage:
    To use the `db` object, simply import it from this module and use it in your
    Flask application:

    ```python
    from extensions import db

    # Example usage
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
    ```
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
