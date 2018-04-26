from flask import abort
from flask_login import current_user
from functools import wraps
from .models import User

def test(role):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kw):
            if current_user.is_authenticated and role <= current_user.role:
                return func(*args, **kw)
            abort(404)
        return wrapper
    return decorate

staff_required = test(User.ROLE_STAFF)
admin_required = test(User.ROLE_ADMIN)
