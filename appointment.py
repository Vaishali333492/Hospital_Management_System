from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.healthcare_db

# Insert an appointment
appointment = {
    "patient_id": "P123456",
    "doctor_id": "D987654",
    "date": datetime(2025, 4, 25, 10, 30),
    "status": "Scheduled",
    "reason": "Fever and headache",
    "department": "General Medicine"
}

db.appointments.insert_one(appointment)
print("Appointment inserted successfully!")
