def remove_book(self, book_id):
        """
        Rimuove un libro dal database in base all'ID del libro fornito.
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
        self.cursor.execute('''
                DELETE FROM books WHERE id = ?
            ''', (book_id,))
        self.connection.commit()