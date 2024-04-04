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

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret_key'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"
# login_manager.session_protection = "strong"

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

@app.route('/')
def index():
  """
  Renders the index.html template.

  Returns:
    The rendered index.html template.
  """
  print('Hello')
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

@app.route('/login', methods=['GET', 'POST'])
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
      return redirect(url_for('view_messages'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  """
  Logs out the current user.

  Returns:
    A redirect to the index route.
  """
  logout_user()
  return redirect(url_for('index'))

@app.route('/messages')
@login_required
def view_messages():
  """
  Renders the messages.html template with all the messages from the database.

  Returns:
    The rendered messages.html template.
  """
  messages = Message.query.all()
  return render_template('messages.html', results=messages)


@app.route('/messages/<message_id>', methods=['GET', 'POST'])
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

@app.route('/blog')
def blog():
  """
  Renders the blog/index.html template with all the blog posts from the database.

  Returns:
    The rendered blog/index.html template.
  """
  # Fetch blog posts from database (replace with actual query)
  posts = 1  # BlogPost.query.all()
  return render_template('blog/index.html', posts=posts)


@app.route('/blog/<blog_post_name>')
def blog_post(blog_post_name):
  """
  Renders the blog/post.html template with a specific blog post from the database.

  Args:
    blog_post_name (str): The name of the blog post.

  Returns:
    The rendered blog/post.html template.
  """
  # Fetch specific blog post from database (replace with actual query)
  post = BlogPost.query.get(blog_post_name)
  if not post:
    return abort(404)
  return render_template('blog/post.html', post=post)

def add_admin():
  """
  Add an admin user to the database.

  This function is used to create an admin user with a password for logging in to the application.
  """
  user = User.query.filter_by(id=1).first()
  if not user:
    user = User(id=1)
    user.set_password('LegoLand2004')
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    add_admin()
  app.run(debug=True)
