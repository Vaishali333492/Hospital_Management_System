import jwt
import datetime
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "e66160e5a671aaab8b87fa021032f40854ceab71021908b3c2e8911d87275a40"

# Decorator for role-based access control
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        # Check if token is provided in the header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            # Decode the JWT token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['username']
        except Exception as e:
            return jsonify({"message": "Token is invalid!"}), 401
        
        return f(current_user, *args, **kwargs)
    
    return decorated_function

# Function to generate JWT token
def generate_token(username, role):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({
        'username': username,
        'role': role,
        'exp': expiration_time
    }, SECRET_KEY, algorithm='HS256')
    return token
