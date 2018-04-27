from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms import TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from .models import User, db, Course

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 22)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self, f):
        if User.query.filter_by(name=f.data).first():
            raise ValidationError('用户名已存在')

    def validate_email(self, f):
        if User.query.filter_by(email=f.data).first():
            raise ValidationError('邮箱已被注册')

    def create_user(self):
        user = User()
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()

class LoginForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 22)])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_name(self, f):
        if not User.query.filter_by(name=f.data).first():
            raise ValidationError('用户名不存在')

    def validate_password(self, f):
        user = User.query.filter_by(name=self.name.data).first()
        if user and not user.check_password(f.data):
            raise ValidationError('密码错误')

class CourseForm(FlaskForm):
    name = StringField('课程名儿', validators=[Required(), Length(6, 33)])
    description = TextAreaField('课程简介', validators=[Required(), Length(20, 233)])
    image_url = StringField('图片地址', validators=[Required(), URL()])
    author_id = IntegerField('作者ID', validators=[Required(), NumberRange(min=1, message='无效的用户ID')])
    submit = SubmitField('提交')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('用户不存在')

    def validate_name(self,f):
        if Course.query.filter_by(name=f.data).first():
            raise ValidationError('课程已经存在')

    def create_course(self):
        course = Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course
