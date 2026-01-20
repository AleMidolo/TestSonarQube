def search_student_by_name(self, name):
    """
    Busca un estudiante en la tabla "students" por su nombre.
    :param name: str, el nombre del estudiante a buscar.
    :return: lista de tuplas, las filas de la tabla "students" que coinciden con los criterios de búsqueda.
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> result = processor.search_student_by_name("John")
    """
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    return results