import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# ✅ Set some patient data (key-value)
r.set("patient:P123456:name", "Vaishali Saini")
r.set("patient:P123456:age", "28")
r.set("patient:P123456:condition", "Hypertension")

# ✅ Retrieve data
name = r.get("patient:P123456:name")
age = r.get("patient:P123456:age")
condition = r.get("patient:P123456:condition")

print(f"Patient Name: {name}")
print(f"Age: {age}")
print(f"Condition: {condition}")
