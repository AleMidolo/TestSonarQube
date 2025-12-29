def create_table(self):
    """
        如果书籍表在数据库中尚不存在，则创建该表。
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS books (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                title TEXT NOT NULL,\n                author TEXT NOT NULL,\n                available INTEGER NOT NULL DEFAULT 1\n            )\n        ')
    self.connection.commit()