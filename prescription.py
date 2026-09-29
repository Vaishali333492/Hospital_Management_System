from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client.healthcare_db

# Insert a prescription
prescription = {
    "patient_id": "P123456",
    "doctor_id": "D987654",
    "date": datetime.today().strftime('%Y-%m-%d'),
    "medicines": [
        {
            "name": "Paracetamol 500mg",
            "dosage": "Twice a day after meals",
            "duration": "5 days"
        },
        {
            "name": "Cough Syrup",
            "dosage": "10ml three times a day",
            "duration": "7 days"
        }
    ],
    "notes": "Plenty of fluids and rest recommended."
}

db.prescriptions.insert_one(prescription)
print("Prescription inserted successfully!")
