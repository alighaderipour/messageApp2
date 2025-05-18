from flask import Blueprint, request, jsonify
from models import User, db
from werkzeug.security import generate_password_hash

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/create_user', methods=['POST'])
def create_user():
    data = request.json
    user = User(username=data.get("username"), password_hash=generate_password_hash(data.get("password")), is_admin=data.get("is_admin", False))
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"})
