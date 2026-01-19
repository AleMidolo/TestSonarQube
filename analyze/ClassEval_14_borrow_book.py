def borrow_book(self, book_id):
    """
    Marks a book as borrowed in the database based on the given book ID.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.borrow_book(1)
    """
    cursor = self.connection.cursor()
    cursor.execute("UPDATE books SET borrowed = 1 WHERE id = ?", (book_id,))
    self.connection.commit()