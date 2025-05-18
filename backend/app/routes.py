@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"message": "Login successful", "user": {"id": user.id, "username": user.username}})
    
    return jsonify({"error": "Invalid credentials"}), 401
