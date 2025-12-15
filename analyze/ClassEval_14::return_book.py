def return_book(self, book_id):
    """
    Segna un libro come restituito nel database in base all'ID del libro fornito.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    self.cursor.execute('''
            UPDATE books SET available = 1 WHERE id = ?
        ''', (book_id,))
    self.connection.commit()