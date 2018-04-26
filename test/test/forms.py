from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, Email, EqualTo, Required
from .models import User, db

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[Required(), Length(3, 22)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_name(self, f):
        if User.query.filter_by(name=f.data).first():
            return ValidationError('用户名已存在')

    def validate_email(self, f):
        if User.query.filter_by(email=f.data).first():
            return ValidationError('邮箱已被注册')

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
            return ValidationError('用户名不存在')

    def validate_password(self, f):
        user = User.query.filter_by(name=self.name.data).first()
        if user and not user.check_password(f.data):
            return ValidationError('密码错误')
