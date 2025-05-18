from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import User, db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    if user and check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"message": "Login successful", "user": {"id": user.id, "username": user.username}})
    return jsonify({"error": "Invalid credentials"}), 401
