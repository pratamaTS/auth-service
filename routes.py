from flask import Blueprint, jsonify, request
from data.login import check_login

bp = Blueprint('routes', __name__)

@bp.route('/health', methods=['GET'])
def health_check_route():
    return jsonify("OK"), 200

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Perform login check using the check_login function
    if check_login(username, password):
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        return jsonify({"message": "Authentication failed", "status": "error"}), 401