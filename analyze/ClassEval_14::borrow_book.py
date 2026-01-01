def borrow_book(self, book_id):
    """
        Marca un libro como prestado en la base de datos según el ID del libro dado.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
    self.cursor.execute('\n                UPDATE books SET available = 0 WHERE id = ? AND available = 1\n            ', (book_id,))
    self.connection.commit()