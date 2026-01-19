def return_book(self, book_id):
    """
    Segna un libro come restituito nel database in base all'ID del libro fornito.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.return_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE books SET borrowed = 0 WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()