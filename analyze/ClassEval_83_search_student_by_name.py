def search_student_by_name(self, name):
    """
    Cerca uno studente nella tabella "students" in base al nome.
    :param name: str, il nome dello studente da cercare.
    :return: lista di tuple, le righe dalla tabella "students" che corrispondono ai criteri di ricerca.
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> result = processor.search_student_by_name("John")
    """
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    return results