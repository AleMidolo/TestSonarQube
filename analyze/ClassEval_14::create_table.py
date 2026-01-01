def create_table(self):
    """
        Creates the book table in the database if it does not already exist.
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS books (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                title TEXT NOT NULL,\n                author TEXT NOT NULL,\n                available INTEGER DEFAULT 1\n            )\n        ')
    self.connection.commit()