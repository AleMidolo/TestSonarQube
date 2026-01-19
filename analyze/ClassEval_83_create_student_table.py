def create_student_table(self):
    """
    Crea una tabella "students" nel database se non esiste già. I campi includono ID di tipo int, nome di tipo str, età di tipo int, genere di tipo str e voto di tipo int.
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    cursor = self.connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    """)
    self.connection.commit()