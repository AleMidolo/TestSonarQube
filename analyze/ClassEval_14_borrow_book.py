def borrow_book(self, book_id):
    """
        Marks a book as borrowed in the database based on the given book ID.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
    self.cursor.execute('\n                UPDATE books SET available = 0 WHERE id = ?\n            ', (book_id,))
    self.connection.commit()