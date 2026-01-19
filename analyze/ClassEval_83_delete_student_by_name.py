def delete_student_by_name(self, name):
    """
    Elimina uno studente dalla tabella "students" in base al nome.
    :param name: str, il nome dello studente da eliminare.
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
    >>> processor.insert_student(student_data)
    >>> processor.delete_student_by_name("John")
    """
    cursor = self.connection.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    self.connection.commit()