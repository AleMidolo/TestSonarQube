def remove_book(self, book_id):
    """
    Removes a book from the database based on the given book ID.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.remove_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()