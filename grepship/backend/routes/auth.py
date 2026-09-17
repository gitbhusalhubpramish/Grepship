from flask import Blueprint, jsonify, request, session 
from models.user import create_user, find_user_by_email, find_user_by_username, find_user_by_id
from utils.security import hash_password, verify_password

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"success": False, "error": "username, email, and password are required"}), 400
    
    existing_email = find_user_by_email(email)
    if existing_email:
        return jsonify({"success": False, "error": "Email already in use"}), 409
    
    existing_user = find_user_by_username(username)
    if existing_user:
        return jsonify({"success": False, "error": "Username already taken"}), 409

    password_hash = hash_password(password)
    user_id = create_user(username, email, password_hash)
    return jsonify({"success": True, "userId": user_id}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get('email')
    password  = data.get("password")

    if not email or not password:
        return jsonify({"success": False, "error": "email and password are required"}), 400

    user = find_user_by_email(email)
    if not user:
        return jsonify({"success": False, "error": "Invalid credentials"}), 401
    
    if not verify_password(password, user['password_hash']):
        return jsonify({"success": False, "error": "Invalid credentials"}), 401
    
    session["user_id"] = str(user["_id"])

    return jsonify({
        "success": True,
        "user": {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "profile_pic": user['profile_pic']
        }
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"success": True}), 200

@auth_bp.route("/me", methods=["GET"])
def me():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"success": False, "error": "Not authenticated"}), 401
    
    user = find_user_by_id(user_id)
    if not user:
        session.clear()
        return jsonify({"success": False, "error": "Not authenticated"}), 401
    
    return jsonify({
        "success": True,
        "user": {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user['email'],
            "profile_pic": user["profile_pic"],
        }
    }), 200