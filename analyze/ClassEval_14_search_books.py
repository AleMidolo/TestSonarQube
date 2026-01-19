def search_books(self):
    """
    Recupera tutti i libri dal database e restituisce le loro informazioni.
    :return books: list[tuple], le informazioni di tutti i libri nel database
    >>> book_db.search_books()
    [(1, 'book1', 'autore', 1)]
    """
    cursor = self.conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return books