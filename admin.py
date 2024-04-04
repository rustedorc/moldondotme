from os import environ
from flask import Blueprint, render_template, request, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required

from extensions import db, login_manager
from models import Message, User

admin = Blueprint('admin', __name__)

@login_manager.user_loader
def load_user(user_id):
  """
  Load a user object from the database.

  Args:
    user_id (int): The unique identifier of the user.

  Returns:
    The user object associated with the given user_id.
  """
  return User.query.get(int(user_id))

@admin.route('/login', methods=['GET', 'POST'])
def login():
  """
  Renders the login.html template.

  Returns:
    The rendered login.html template.
  """
  if request.method == 'POST':
    password = request.form['password']
    user = User.query.filter_by(id=1).first()
    if user and user.check_password(password):
      login_user(user)
      return redirect(url_for('admin.view_messages'))
  return render_template('login.html')

@admin.route('/logout')
def logout():
  """
  Logs out the current user.

  Returns:
    A redirect to the index route.
  """
  logout_user()
  return redirect(url_for('index'))

@admin.route('/messages')
@login_required
def view_messages():
  """
  Renders the messages.html template with all the messages from the database.

  Returns:
    The rendered messages.html template.
  """
  messages = Message.query.all()
  return render_template('messages.html', results=messages)


@admin.route('/messages/<message_id>', methods=['GET', 'POST'])
def delete_message(message_id):
  """
  Deletes a message from the database.

  Args:
    message_id (int): The unique identifier of the message to delete.

  Returns:
    A redirect to the view_messages route.
  """
  message = Message.query.get(message_id)
  if not message:
    return abort(404)
  db.session.delete(message)
  db.session.commit()
  return redirect(url_for('view_messages'))

def add_admin():
  """
  Add an admin user to the database.

  This function is used to create an admin user with a password for logging in to the application.
  """
  user = User.query.filter_by(id=1).first()
  if not user:
    user = User(id=1)
    user.set_password(environ.get('ADMIN_PASSWORD'))
    db.session.add(user)
    db.session.commit()