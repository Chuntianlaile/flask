from flask import Blueprint, render_template
from test.models import Course

course = Blueprint('course', __name__, url_prefix='/course')

@course.route('/<int:course_id>')
def detail(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course/detail.html', course=course)
