from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper


def get_current_user():
    return get_jwt_identity()
