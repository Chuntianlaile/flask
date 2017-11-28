from flask import Blueprint, render_template
from simpledu.models import Course

course = Blueprint('course', __name__, url_prefix='/course')

@course.route('/<id>')
def index(id):
    course = Course.query.get_or_404(id)
    render_template('course.html', course=course)
