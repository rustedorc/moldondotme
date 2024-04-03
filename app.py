"""
This module contains a Flask application for a portfolio website.

The application includes routes for rendering different templates, handling a contact form submission,
viewing messages, and displaying blog posts.

Author: [Your Name]
"""

from flask import Flask, render_template, abort, request
from extensions import db
from models import BlogPost, Message

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)

# Rest of the code...
from flask import Flask, render_template, abort, request
from extensions import db
from models import BlogPost, Message

app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)


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


@app.route('/messages')
def view_messages():
  """
  Renders the messages.html template with all the messages from the database.

  Returns:
    The rendered messages.html template.
  """
  messages = Message.query.all()
  return render_template('messages.html', results=messages)


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


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
