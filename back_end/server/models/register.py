from flask import request, jsonify
from flask_restful import Resource
from models.user import User
from .conn import db

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'employee')  # ✅ Default role is 'employee'

        if not username or not email or not password:
            return {"message": "Missing fields"}, 400

        if User.query.filter((User.username == username) | (User.email == email)).first():
            return {"message": "User already exists"}, 400

        new_user = User(username=username, email=email, role=role)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict(), 201
