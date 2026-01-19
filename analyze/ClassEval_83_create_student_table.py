def create_student_table(self):
    """
        Creates a table "students" in the database if it does not already exist. The fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = '\n        CREATE TABLE IF NOT EXISTS students (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            name TEXT NOT NULL,\n            age INTEGER NOT NULL,\n            gender TEXT NOT NULL,\n            grade INTEGER NOT NULL\n        )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()