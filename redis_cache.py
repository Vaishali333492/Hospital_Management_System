import redis
import json

# Connect to Redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Cache patient info in Redis
def cache_patient(patient_id):
    cached_patient = r.get(patient_id)
    if cached_patient:
        return json.loads(cached_patient)
    return None

# Set patient info in Redis
def set_patient_cache(patient_id, patient_data):
    r.set(patient_id, json.dumps(patient_data))
