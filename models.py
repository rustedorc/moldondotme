from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

blogpost_tabs = db.Table('blogpost_tags',
                         db.Column('tag_id', db.Integer, db.ForeignKey(
                             'tags.id'), primary_key=True),
                         db.Column('blogpost_id', db.Integer, db.ForeignKey(
                             'blogposts.id'), primary_key=True))


class Tag(db.Model):
    """
    Represents a tag that can be associated with a blog post.

    Attributes:
        id (int): The unique identifier of the tag.
        name (str): The name of the tag.
    """

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Tag: {self.name}>'


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
    tags = db.relationship('Tag', secondary='blogpost_tags',
                           backref=db.backref('blogposts', lazy=True))

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
    time_sent = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Message({self.id=}, {self.name=}, {self.email=}, {self.message=})>'

    def to_json(self) -> dict[str, str]:
        """
        Convert the object to a JSON-compatible dictionary.

        Returns:
            A dictionary containing the object's attributes in a JSON-compatible format.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message,
            'time_sent': self.time_sent.strftime('%d-%m-%Y %H:%M:%S')
        }


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f'User({self.id})'
