#!/usr/bin/env python3
"""Session Auth"""

from api.v1.views import app_views
from flask import jsonify, request
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """ POST /api/v1/auth/session/login
    Return user instance, 400 if missing
    """
    user_email = request.form.get('email', None)
    user_password = request.form.get('password', None)

    if user_email is None or user_email == "":
        return jsonify({"error": "email missing"}), 400
    if user_password is None or user_password == "":
        return jsonify({"error": "password missing"}), 400

    is_valid_user = User.search({'email': user_email})

    if not is_valid_user:
        return jsonify({"error": "no user found for this email"}), 404

    is_valid_user = is_valid_user[0]

    if not is_valid_user.is_valid_password(user_password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(is_valid_user.id)
    cookie_response = getenv('SESSION_NAME')
    user_dict = jsonify(is_valid_user.to_json())

    user_dict.set_cookie(cookie_response, session_id)
    return user_dict
