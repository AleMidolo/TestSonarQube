def create_student_table(self):
    """
        Crea una tabella "students" nel database se non esiste già. I campi includono ID di tipo int, nome di tipo str, età di tipo int, genere di tipo str e voto di tipo int.
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