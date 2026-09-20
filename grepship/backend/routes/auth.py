from flask import Blueprint, jsonify, request, session
from models.user import create_user, find_user_by_email_or_username, find_user_by_id
from utils.security import hash_password, verify_password
from utils.validation import get_str, valid_username, valid_email
from utils.password import check_password_strength

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/signup", methods=["POST"])
def register():
    data = request.get_json(silent=True) or {}
    if not data:
        return jsonify({"success": False, "error": "Invalid JSON body"}), 400

    username = get_str(data, "username")
    email = get_str(data, "email").lower()
    password = get_str(data, "password", strip=False)

    if not username or not password:
        return jsonify({"success": False, "error": "username and password are required"}), 400

    if not valid_username(username):
        return jsonify({"success": False, "error": "username must be 3-20 chars: a-z, 0-9, _"}), 400

    ok, err = check_password_strength(password)
    if not ok:
        return jsonify({"success": False, "error": err}), 400

    if email and not valid_email(email):
        return jsonify({"success": False, "error": "Invalid email format"}), 400
    if len(email) > 254:
        return jsonify({"success": False, "error": "email too long"}), 400

    if find_user_by_email_or_username(username=username):
        return jsonify({"success": False, "error": "Username already taken"}), 409
    
    if email and find_user_by_email_or_username(email=email):
        return jsonify({"success": False, "error": "Email already in use"}), 409

    password_hash = hash_password(password)
    user_id = create_user(username, email or None, password_hash)
    return jsonify({"success": True, "userId": user_id}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"success": False, "error": "Invalid JSON body"}), 400

    username = get_str(data, "username")
    password = get_str(data, "password", strip=False)

    if not username or not password:
        return jsonify({"success": False, "error": "username and password are required"}), 400

    if len(username) > 20 or len(password) > 100:
        return jsonify({"success": False, "error": "Invalid credentials"}), 401

    user = find_user_by_email_or_username(username=username)
    if not user:
        return jsonify({"success": False, "error": "Invalid credentials"}), 401

    if not verify_password(password, user["password_hash"]):
        return jsonify({"success": False, "error": "Invalid credentials"}), 401

    session["user_id"] = str(user["_id"])

    return jsonify({
        "success": True,
        "user": {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user.get('email'),
            "profile_pic": user["profile_pic"],
        }
    }), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True}), 200

@auth_bp.route("/me", methods=["GET"])
def me():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"user": None}), 200

    user = find_user_by_id(user_id)
    if not user:
        session.clear()
        return jsonify({"user": None}), 200

    return jsonify({
        "user": {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user.get('email') or None,
            "profile_pic": user["profile_pic"],
        }
    }), 200
