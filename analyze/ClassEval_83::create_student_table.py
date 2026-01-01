def create_student_table(self):
    """
        Crea una tabla "students" en la base de datos si no existe ya. Los campos incluyen ID de tipo int, nombre de tipo str, edad de tipo int, género de tipo str y grado de tipo int.
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