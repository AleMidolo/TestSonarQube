def create_student_table(self):
    """
        如果数据库中尚不存在，则创建一个“students”表。字段包括类型为int的ID，类型为str的姓名，类型为int的年龄，类型为str的性别，以及类型为int的年级。
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """
    conn = sqlite3.connect(self.database_name)
    cursor = conn.cursor()
    create_table_query = '\n        CREATE TABLE IF NOT EXISTS students (\n            id INTEGER PRIMARY KEY AUTOINCREMENT,\n            name TEXT NOT NULL,\n            age INTEGER NOT NULL,\n            gender TEXT NOT NULL,\n            grade INTEGER NOT NULL\n        )\n        '
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()