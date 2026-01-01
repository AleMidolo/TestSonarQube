def search_student_by_name(self, name):
    """
        "students" तालिका में छात्र को उनके नाम से खोजता है।
        :param name: str, खोजने के लिए छात्र का नाम।
        :return: ट्यूपल की सूची, "students" तालिका की वे पंक्तियाँ जो खोज मानदंड से मेल खाती हैं।
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