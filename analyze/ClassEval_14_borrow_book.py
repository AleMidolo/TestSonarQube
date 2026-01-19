def borrow_book(self, book_id):
    """
        दिए गए पुस्तक आईडी के आधार पर डेटाबेस में एक पुस्तक को उधार लिया गया के रूप में चिह्नित करता है।
        :param book_id: int
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.borrow_book(1)
        """
    self.cursor.execute('\n                UPDATE books SET available = 0 WHERE id = ? AND available = 1\n            ', (book_id,))
    self.connection.commit()