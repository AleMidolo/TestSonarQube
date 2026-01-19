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
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?)
    """, (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
    
    conn.commit()
    conn.close()