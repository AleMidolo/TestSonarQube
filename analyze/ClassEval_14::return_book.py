def return_book(self, book_id):
    """
        दिए गए पुस्तक आईडी के आधार पर डेटाबेस में एक पुस्तक को वापस किया गया के रूप में चिह्नित करता है।
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.return_book(1)
        """
    self.cursor.execute('\n                UPDATE books SET available = 1 WHERE id = ?\n            ', (book_id,))
    self.connection.commit()