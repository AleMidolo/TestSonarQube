def borrow_book(self, book_id):
    """
    Segna un libro come preso in prestito nel database in base all'ID del libro fornito.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.borrow_book(1)
    """
    self.cursor.execute('\n            UPDATE books SET available = 0 WHERE id = ?\n        ', (book_id,))
    self.connection.commit()