import sqlite3


class StudentDatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            create_table_query = self._get_create_table_query()
            cursor.execute(create_table_query)

    def insert_student(self, student_data):
        with self._connect() as conn:
            cursor = conn.cursor()
            insert_query = self._get_insert_query()
            cursor.execute(insert_query, self._get_student_values(student_data))

    def search_student_by_name(self, name):
        with self._connect() as conn:
            cursor = conn.cursor()
            select_query = "SELECT * FROM students WHERE name = ?"
            cursor.execute(select_query, (name,))
            return cursor.fetchall()

    def delete_student_by_name(self, name):
        with self._connect() as conn:
            cursor = conn.cursor()
            delete_query = "DELETE FROM students WHERE name = ?"
            cursor.execute(delete_query, (name,))
    
    def _connect(self):
        return sqlite3.connect(self.database_name)

    def _get_create_table_query(self):
        return """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
        """

    def _get_insert_query(self):
        return """
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?)
        """

    def _get_student_values(self, student_data):
        return (student_data['name'], student_data['age'], student_data['gender'], student_data['grade'])