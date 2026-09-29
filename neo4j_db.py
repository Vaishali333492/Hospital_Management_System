from neo4j import GraphDatabase

# Connect to Neo4j
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j_password"))

# Get patients for a specific doctor
def get_doctor_patients(doctor_name):
    with driver.session() as session:
        query = """
        MATCH (d:Doctor)-[:TREATS]->(p:Patient)
        WHERE d.name = $doctor_name
        RETURN p.patient_id AS patient_id, p.name AS name, p.condition AS condition
        """
        result = session.run(query, doctor_name=doctor_name)
        patients = [{"patient_id": record["patient_id"], "name": record["name"], "condition": record["condition"]} for record in result]
        return patients
