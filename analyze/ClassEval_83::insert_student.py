def insert_student(self, student_data):
    """
        Inserisce un nuovo studente nella tabella "students".
        :param student_data: dict, un dizionario contenente le informazioni dello studente (nome, età, genere, voto).
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    insert_query = '\n            INSERT INTO students (name, age, gender, grade)\n            VALUES (?, ?, ?, ?)\n        '
    cursor.execute(insert_query, (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
    conn.commit()
    conn.close()