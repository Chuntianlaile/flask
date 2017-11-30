from flask import Blueprint, render_template
from simpledu.models import Course

course = Blueprint('course', __name__, url_prefix='/course')

@course.route('/<id>')
def index(id):
    course = Course.query.get_or_404(id)
    return render_template('course.html', course=course)

@course.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
