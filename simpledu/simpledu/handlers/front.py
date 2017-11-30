from flask import Blueprint, render_template, abort
from simpledu.models import Course, User

front = Blueprint('front', __name__)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)
