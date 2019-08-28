    

from app import db
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from base import Base,engine

from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ ='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(64),index=True , unique=True)
    email=Column(String(120),index=True , unique=True)
    post=relationship('Post',backref='users',lazy='dynamic')
    password_hash=Column(String(128))
 
def __repr__(self):
    return'<User {}>'.format(self.username)
 
def __init__(self,username,email,name,password):
    self.username=username
    self.email=email
    self.name=name
    self.password_hash=hash(password)
 
#class Post(db.Model):
    #__tablename__='post'
    #id=Column(Integer,primary_key=True)
    #username=Column(String(130), index=True)
    #password_hash=Column(String(128))
    #name=Column(String(50), index=True)
    #email = Column(String(120), index=True, unique=True)
    #user_id=Column(Integer,ForeignKey('user.id'))

#def __repr__(self):
    #return'<Post> {}'.format(self.body)
 
#def __init__(self,title,body,user_id):
    #self.titile=title
    #self.body=body
    #self.timestamp=datetime.utcnow()
    #self.user_id=user_id


Base.metadata.create_all(engine)

