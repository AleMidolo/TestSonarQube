def create_table(self):
    """
    Creates the book table in the database if it does not already exist.
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
            publication_year INTEGER,
            quantity INTEGER DEFAULT 0
        )
    ''')
    self.connection.commit()