from flask import Blueprint, render_template, current_app, request
from flask import flash, redirect, url_for
from test.decorators import admin_required
from test.models import Course, db, User
from test.forms import CourseForm

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/courses')
@admin_required
def course():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/course.html', pagination=pagination)

@admin.route('/courses/create', methods=['GET', 'POST'])
@admin_required
def create():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('成功添加课程：{}'.format(form.name.data), 'success')
        return redirect(url_for('.course'))
    return render_template('admin/create.html', form=form)

@admin.route('/courses/<int:course_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit(course_id):
    course = Course.query.get_or_404(course_id)
    form = CourseForm(obj=course)
    if form.validate_on_submit():
        form.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        flash('成功编辑课程。', 'success')
        return redirect(url_for('.course'))
    return render_template('admin/edit.html', course=course, form=form)

@admin.route('/courses/<int:course_id>/delete')
@admin_required
def delete(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('成功删除课程：{}'.format(course.name), 'info')
    return redirect(url_for('.course'))
