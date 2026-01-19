def search_student_by_name(self, name):
    """
    Searches for a student in the "students" table by their name.
    :param name: str, the name of the student to search for.
    :return: list of tuples, the rows from the "students" table that match the search criteria.
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> result = processor.search_student_by_name("John")
    """
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    return result