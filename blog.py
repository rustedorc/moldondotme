from flask import Blueprint, render_template, abort
from models import BlogPost

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
  """
  Renders the blog/index.html template with all the blog posts from the database.

  Returns:
    The rendered blog/index.html template.
  """
  # Fetch blog posts from database (replace with actual query)
  posts = BlogPost.query.count()
  return render_template('blog/index.html', num_of_posts=posts)

@blog.route('<blog_post_name>')
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