def search_student_by_name(self, name):
    """
    "students" तालिका में छात्र को उनके नाम से खोजता है।
    :param name: str, खोजने के लिए छात्र का नाम।
    :return: ट्यूपल की सूची, "students" तालिका की वे पंक्तियाँ जो खोज मानदंड से मेल खाती हैं।
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> result = processor.search_student_by_name("John")
    """
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    return results