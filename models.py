from extensions import db


class BlogPost(db.Model):
    """
    Represents a blog post.

    Attributes:
        id (int): The unique identifier for the blog post.
        title (str): The title of the blog post.
        body (str): The body content of the blog post.
    """

    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<BlogPost: {self.title}>'


class Message(db.Model):
    """
    Represents a message sent by a user.

    Attributes:
        id (int): The unique identifier of the message.
        name (str): The name of the user who sent the message.
        email (str): The email address of the user who sent the message.
        message (str): The content of the message.
    """

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Message({self.id=}, {self.name=}, {self.email=}, {self.message=})>'
