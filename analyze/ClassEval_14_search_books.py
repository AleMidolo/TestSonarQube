def search_books(self):
    """
    Recupera todos los libros de la base de datos y devuelve su información.
    :return books: list[tuple], la información de todos los libros en la base de datos
    >>> book_db.search_books()
    [(1, 'book1', 'author', 1)]
    """
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return books