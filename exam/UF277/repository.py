class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, student_id):
        query = f"SELECT * FROM students WHERE id={student_id}"
        result = self.connector.execute_and_fetchone(query)
        return result