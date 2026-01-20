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
            id INTEGER,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
    ''')
    self.connection.commit()