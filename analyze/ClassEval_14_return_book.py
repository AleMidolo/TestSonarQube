def return_book(self, book_id):
    """
    Marks a book as returned in the database based on the given book ID.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    self.cursor.execute('\n            UPDATE books SET available = 1 WHERE id = ?\n        ', (book_id,))
    self.connection.commit()