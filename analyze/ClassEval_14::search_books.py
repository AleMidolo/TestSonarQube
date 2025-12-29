def search_books(self):
    """
        Recupera tutti i libri dal database e restituisce le loro informazioni.
        :return books: list[tuple], le informazioni di tutti i libri nel database
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.add_book('book1', 'author')
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
    self.cursor.execute('SELECT * FROM books')
    books = self.cursor.fetchall()
    return books