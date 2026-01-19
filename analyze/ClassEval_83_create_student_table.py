def create_student_table(self):
    """
        यदि "students" तालिका पहले से मौजूद नहीं है, तो डेटाबेस में "students" तालिका बनाता है। फ़ील्ड में int प्रकार का ID, str प्रकार का नाम, int प्रकार की उम्र, str प्रकार का लिंग, और int प्रकार का ग्रेड शामिल हैं।
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = '\n            CREATE TABLE IF NOT EXISTS students (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                name TEXT NOT NULL,\n                age INTEGER NOT NULL,\n                gender TEXT NOT NULL,\n                grade INTEGER NOT NULL\n            )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()