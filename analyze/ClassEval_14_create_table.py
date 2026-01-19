def create_table(self):
    """
    Crea la tabella dei libri nel database se non esiste già.
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    """
    cursor = self.conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT UNIQUE
        )
    ''')
    self.conn.commit()