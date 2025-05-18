from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User, db

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"message": "Login successful", "user": {"id": user.id, "username": user.username}})
    
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data.get("username")).first():
        return jsonify({"error": "Username already exists"}), 400
    
    hashed_password = generate_password_hash(data.get("password"))
    new_user = User(username=data.get("username"), password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"})
