def delete_student_by_name(self, name):
    """
    "students" तालिका से छात्र को उनके नाम द्वारा हटाता है।
    :param name: str, हटाने के लिए छात्र का नाम।
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