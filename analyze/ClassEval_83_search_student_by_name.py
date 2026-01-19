def search_student_by_name(self, name):
    """
    根据学生的姓名在"students"表中搜索学生。
    :param name: str，要搜索的学生姓名。
    :return: list of tuples，符合搜索条件的"students"表中的行。
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    >>> result = processor.search_student_by_name("John")
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
    results = cursor.fetchall()
    
    conn.close()
    
    return results