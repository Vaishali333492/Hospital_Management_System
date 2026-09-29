from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.healthcare_db
patients_collection = db.patients

# Get patient info by patient_id
def get_patient_by_id(patient_id):
    patient = patients_collection.find_one({"patient_id": patient_id})
    if patient:
        return {
            "patient_id": patient["patient_id"],
            "name": patient["name"],
            "age": patient["age"],
            "condition": patient["condition"]
        }
    return None
