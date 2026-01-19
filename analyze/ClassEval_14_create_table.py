def create_table(self):
    """
    如果书籍表在数据库中尚不存在，则创建该表。
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    """
    cursor = self.connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT,
            publication_date TEXT,
            publisher TEXT
        )
    ''')
    self.connection.commit()