def create_student_table(self):
    """
    Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            ID INTEGER,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
    ''')
    self.connection.commit()