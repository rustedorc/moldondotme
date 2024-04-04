"""
This module contains a Flask application for a portfolio website.

The application includes routes for rendering different templates, handling a contact form submission,
viewing messages, and displaying blog posts.

Author: Tom
"""

from flask import Flask, render_template, abort, request, redirect, url_for
from flask_login import login_required, login_user, logout_user
from extensions import db, login_manager
from models import BlogPost, Message, User
from admin import admin, add_admin
from blog import blog

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(blog, url_prefix='/blog')

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret_key'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "admin.login"



@app.route('/')
def index():
  """
  Renders the index.html template.

  Returns:
    The rendered index.html template.
  """
  return render_template('index.html')


@app.route('/portfolio')
def portfolio():
  """
  Renders the portfolio.html template.

  Returns:
    The rendered portfolio.html template.
  """
  return render_template('portfolio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  """
  Handles the contact form submission.

  If the request method is POST, it validates the form data and saves the message to the database.
  If there are any validation errors, it renders the contact.html template with the error message.
  If the form is successfully submitted, it renders the contact.html template with a success message.

  Returns:
    The rendered contact.html template.
  """
  message_sent = False
  error = False
  if request.method == 'POST':
    name = request.form['name']
    if not name:
      error = 'Name is required.'
    email = request.form['email']
    if not email:
      error = 'Email is required.'
    message_contents = request.form['message']
    if not message_contents:
      error = 'Message is required.'
    if error:
      return render_template('contact.html', error=error)
    message = Message(name=name, email=email, message=message_contents)
    db.session.add(message)
    db.session.commit()
    message_sent = True
  return render_template('contact.html', message_sent=message_sent)


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    add_admin()
  app.run(debug=True)
