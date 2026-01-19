def create_student_table(self):
    """
    Crea una tabella "students" nel database se non esiste già. I campi includono ID di tipo int, nome di tipo str, età di tipo int, genere di tipo str e voto di tipo int.
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
    ''')
    self.connection.commit()