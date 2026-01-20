def create_student_table(self):
    """
    Crea una tabla "students" en la base de datos si no existe ya. Los campos incluyen ID de tipo int, nombre de tipo str, edad de tipo int, género de tipo str y grado de tipo int.
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    ''')
    self.connection.commit()