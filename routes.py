from flask import Blueprint, jsonify, request
from data.login import check_login, update_user_token
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('routes', __name__)

@bp.route('/health', methods=['GET'])
def health_check_route():
    return jsonify("OK"), 200

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = check_login(username, password)
    # Perform login check using the check_login function
    if user_data:
        access_token = create_access_token(identity=username)

        # Update the user data with the token
        user_data['access_token'] = access_token

        # Update the user in the database with the token
        update_user_token(user_data)

        return jsonify({
            "error": False,
            "message": "Succesfully login",
            "access_token": access_token
        }), 200
    else:
        return jsonify({"message": "Authentication failed", "status": "error"}), 401

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    # Access this route only if a valid access token is provided
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello, {current_user}! This is a protected route."}), 200