def remove_book(self, book_id):
    """
    Rimuove un libro dal database in base all'ID del libro fornito.
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