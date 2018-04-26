from flask import Blueprint, render_template, flash, url_for, redirect
from flask_login import login_user, logout_user, login_required
from test.models import User, db, Course
from test.forms import LoginForm, RegisterForm

front = Blueprint('front', __name__)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.name.data.isalnum():
            flash('名字只能由数字和字母组成。', 'info')
            return redirect(url_for('.register'))
        form.create_user()
        flash('注册成功，请登录。', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        login_user(user, form.remember_me.data)
        flash('登录成功。', 'success')
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已退出登录。', 'success')
    return redirect(url_for('.index'))
