from datetime import datetime
from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(Base, UserMixin):
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    job = db.Column(db.String(128))
    course = db.relationship('Course')

    def __repr__(self):
        return 'User: {}'.format(self.name)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, p):
        self._password = generate_password_hash(p)

    def check_password(self, p):
        return check_password_hash(self._password, p)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN
        
    @property
    def is_staff(self):
        return self.role == self.ROLE_STAFF

class Course(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    description = db.Column(db.String(256))
    image_url = db.Column(db.String(256))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)
    chapter = db.relationship('Chapter')

    @property
    def url(self):
        return url_for('course.detail', course_id=self.id)

    def __repr__(self):
        return 'Course: {}'.format(self.name)

class Chapter(Base):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    video_url = db.Column(db.String(256))
    video_duration = db.Column(db.String(64))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'))
    course = db.relationship('Course')

    def __repr__(self):
        return 'Chapter: {}'.format(self.name)
