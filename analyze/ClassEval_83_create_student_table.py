def create_student_table(self):
    """
    如果数据库中尚不存在,则创建一个"students"表。字段包括类型为int的ID,类型为str的姓名,类型为int的年龄,类型为str的性别,以及类型为int的年级。
    :return: None
    >>> processor = StudentDatabaseProcessor("students.db")
    >>> processor.create_student_table()
    """
    import sqlite3
    
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