def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """
        
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        
        search_query = "SELECT * FROM students WHERE name = ?"
        cursor.execute(search_query, (name,))
        results = cursor.fetchall()
        
        conn.close()
        return results