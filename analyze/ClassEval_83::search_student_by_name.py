def search_student_by_name(self, name):
    """
        Busca un estudiante en la tabla "students" por su nombre.
        :param name: str, el nombre del estudiante a buscar.
        :return: lista de tuplas, las filas de la tabla "students" que coinciden con los criterios de búsqueda.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    search_query = 'SELECT * FROM students WHERE name = ?'
    cursor.execute(search_query, (name,))
    results = cursor.fetchall()
    conn.close()
    return results