def create_table(self):
    """
        Crea la tabla de libros en la base de datos si no existe ya.
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.create_table()
        """
    self.cursor.execute('\n            CREATE TABLE IF NOT EXISTS books (\n                id INTEGER PRIMARY KEY AUTOINCREMENT,\n                title TEXT NOT NULL,\n                author TEXT NOT NULL,\n                available INTEGER NOT NULL DEFAULT 1\n            )\n        ')
    self.connection.commit()