def create_table(self):
    """
    Crea la tabla de libros en la base de datos si no existe ya.
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