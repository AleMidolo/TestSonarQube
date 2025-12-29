def remove_book(self, book_id):
    """
        दिए गए पुस्तक आईडी के आधार पर डेटाबेस से एक पुस्तक को हटाता है।
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.remove_book(1)
        """
    self.cursor.execute('\n                DELETE FROM books WHERE id = ?\n            ', (book_id,))
    self.connection.commit()