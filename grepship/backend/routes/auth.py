from flask import Blueprint, jsonify, request, session, make_response
from models.user import create_user, find_user_by_email_or_username, find_user_by_id
from utils.security import hash_password, verify_password
from utils.validation import get_str, valid_username, valid_email
from utils.password import check_password_strength
import traceback
import secrets
from utils.redis import redis_client

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/signup", methods=["POST"])

def register():
    try:
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
        print("pass 409-1")
        if email and find_user_by_email_or_username(email=email):
            return jsonify({"success": False, "error": "Email already in use"}), 409
        print("pass 409-2")
        password_hash = hash_password(password)

        user_id = create_user(username, email or None, password_hash)

        session_id = secrets.token_urlsafe(32)

        response= make_response(jsonify({"message": "Login successful"}))

        response.set_cookie("session_id", session_id, httponly=True, secure=True, samesite="Lax", max_age=7*24*60*60)

        redis_client.setex(f"session{session_id}", 7*24*60*60, username)

        return response, 201
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {"error": str(e)}

@auth_bp.route("/login", methods=["POST"])

def login():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({"success": False, "error": "Invalid JSON body"}), 400

        username = get_str(data["username"])

        password = get_str(data["password"])

        if not username or not password:
            return jsonify({"success": False, "error": "username and password are required"}), 400

        if len(username) > 100 or len(password) > 100 or not valid_username(username) or not valid_password(password):
            return jsonify({"success": False, "error": "Invalid credentials"}), 401

        user = find_user_by_email_or_username(username=username)

        if not user:
            return jsonify({"success": False, "error": "Invalid credentials"}), 401

        if not verify_password(password, user["password_hash"]):
            return jsonify({"success": False, "error": "Invalid credentials"}), 401

        session_id = secrets.token_urlsafe(32)

        response= make_response(jsonify({"message": "Login successful"}))

        response.set_cookie("session_id", session_id, httponly=True, secure=True, samesite="Lax", max_age=7*24*60*60)

        redis_client.setex(f"session{session_id}", 7*24*60*60, username)

        return response, 200
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {"error": str(e)}



@auth_bp.route("/logout", methods=["POST"])

def logout():

    session.clear()

    return jsonify({"success": True}), 200

@auth_bp.route("/me", methods=["GET"])

def me():
    try:
        user_id = request.cookies.get("session_id")

        if not user_id:
            return jsonify({"user": None}), 401

        user = redis_client.get(f"session{user_id}")
        print(user)
        user = find_user_by_email_or_username(username=user)
        print(user_id, user)

        if not user:
            response = make_response(jsonify({"user":None}))
            response.delete_cookie("session_id")
            redis_client.delete(f"session{user_id}")
            return response, 401

        return jsonify({
            "user": {
                "id": str(user["_id"]),
                "username": user["username"],
                "email": user.get('email') or None,
                "profile_pic": user["profile_pic"],            
            }
        }), 200
    except Exception as e:
        traceback.print_exc()
        print(e)
        return {"error": str(e)}

# To work with user authentication eg login and signup page on frontend this file is create. 

# simple code overview
#  -> Register for registering the user mainly after filling signup page
# -> Login for checking a user is exist with username and password or email optional. 
# -> Store in hash password, can failed sql injection, xss and other common attacks.
