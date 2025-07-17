from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from models.user import User

def jwt_required_custom(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        return fn(*args, **kwargs)
    return wrapper

def get_current_user():
    return get_jwt_identity()

def admin_required(fn):  # ✅ Decorator to enforce admin-only access
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user and user.role == 'admin':
            return fn(*args, **kwargs)
        return {"message": "Admin privileges required"}, 403
    return wrapper