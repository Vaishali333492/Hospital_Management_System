from flask import Flask, jsonify, request
from flask_cors import CORS
import bcrypt
from auth import generate_token, token_required
from mongodb import get_patient_by_id
from redis_cache import cache_patient
from neo4j_db import get_doctor_patients

app = Flask(__name__)
CORS(app)

# Temporary user data for testing (In real scenarios, this data would be stored in a DB)
users = {
    "admin": {"password": bcrypt.hashpw("admin_pass".encode('utf-8'), bcrypt.gensalt()), "role": "admin"},
    "doctor1": {"password": bcrypt.hashpw("doctor_pass".encode('utf-8'), bcrypt.gensalt()), "role": "doctor"},
}

@app.route("/")
def index():
    return "Welcome to the Health Care Management API"

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Validate the user credentials
    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]["password"]):
        token = generate_token(username, users[username]["role"])
        return jsonify({"token": token})
    
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route("/api/patient/<patient_id>")
@token_required
def patient_info(current_user, patient_id):
    cached = cache_patient(patient_id)
    if cached:
        return jsonify({"source": "redis", "data": cached})

    patient = get_patient_by_id(patient_id)
    if patient:
        return jsonify({"source": "mongodb", "data": patient})
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/doctor/<doctor_name>/patients")
@token_required
def doctor_patients(current_user, doctor_name):
    # Only allow doctor or admin to access
    if current_user != "admin" and current_user != doctor_name:
        return jsonify({"message": "Unauthorized access!"}), 403

    patients = get_doctor_patients(doctor_name)
    return jsonify({"patients": patients})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
