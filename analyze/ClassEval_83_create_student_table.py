def create_student_table(self):
    """
    यदि "students" तालिका पहले से मौजूद नहीं है, तो डेटाबेस में "students" तालिका बनाता है। फ़ील्ड में int प्रकार का ID, str प्रकार का नाम, int प्रकार की उम्र, str प्रकार का लिंग, और int प्रकार का ग्रेड शामिल हैं।
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
    ''')
    self.connection.commit()