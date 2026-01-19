def delete_student_by_name(self, name):
    """
        Elimina un estudiante de la tabla "students" por su nombre.
        :param name: str, el nombre del estudiante a eliminar.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("John")
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    delete_query = 'DELETE FROM students WHERE name = ?'
    cursor.execute(delete_query, (name,))
    conn.commit()
    conn.close()