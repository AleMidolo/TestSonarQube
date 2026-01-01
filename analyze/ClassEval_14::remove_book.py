def remove_book(self, book_id):
    """
        Elimina un libro de la base de datos según el ID del libro dado.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
    self.cursor.execute('\n                DELETE FROM books WHERE id = ?\n            ', (book_id,))
    self.connection.commit()