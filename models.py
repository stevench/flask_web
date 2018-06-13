# -*- encoding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy(app)


class User(db.Model):
    """Represents Proeced users."""

    #Set the name for table
    __tablename__ = "users"
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    #Establish contact with Post
    posts = db.relationship(
            'Post',
            backref='users',
            lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Model User `{}`>".format(self.username)


posts_tags = db.Table('posts_tags',
      db.Column('post_id', db.String(45), db.ForeignKey('posts.id'))
      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):
    """Represents Proected posts.""" 

    __tablename__ = "posts"
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    #Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey("users.id"))
    #Establish contact with Commit's ForeignKey:post_id
    comments = db.relationship(
            'Comment',
            backref='posts',
            lazy='dynamic')

    #many to many: posts <===> tags
    tags = db.relationship(
            'Tag',
            secondary=posts_tags,
            backref=db.backref('posts', lazy='dynamic'))
   
    def __init__(self, id, title, text, publish_date):
        self.id = id
        self.title = title
        self.text = text
        self.publish_date = publish_date

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)  


class Comment(db.Model):
    """Represents Proected comments."""

    __tablename__ = "comments"
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForiegnKey("posts.id"))

    def __init__(self, id, name, text, date, post_id):
        self.id = id
        self.name = name
        self.text = text
        self.date = date
        self.post_id = post_id

    def __repr__(self):
        return "<Model Comment `{}`>".format(self.name)  
       

class Tag(db.Model):
    """Represents Proected tags.""" 

    __tablename__ = "tags"
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)  
    
