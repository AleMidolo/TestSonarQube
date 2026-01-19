def return_book(self, book_id):
    """
    दिए गए पुस्तक आईडी के आधार पर डेटाबेस में एक पुस्तक को वापस किया गया के रूप में चिह्नित करता है।
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE books SET status = 'available' WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()