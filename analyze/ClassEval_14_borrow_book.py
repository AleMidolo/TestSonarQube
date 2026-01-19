def borrow_book(self, book_id):
    """
    दिए गए पुस्तक आईडी के आधार पर डेटाबेस में एक पुस्तक को उधार लिया गया के रूप में चिह्नित करता है।
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.borrow_book(1)
    """
    cursor = self.connection.cursor()
    cursor.execute("UPDATE books SET is_borrowed = 1 WHERE id = ?", (book_id,))
    self.connection.commit()