def return_book(self, book_id):
    """
    Marks a book as returned in the database based on the given book ID.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE books SET returned = 1 WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()