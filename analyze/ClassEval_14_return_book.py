def return_book(self, book_id):
    """
    Marca un libro como devuelto en la base de datos según el ID del libro dado.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    self.cursor.execute('\n            UPDATE books SET available = 1 WHERE id = ?\n        ', (book_id,))
    self.connection.commit()