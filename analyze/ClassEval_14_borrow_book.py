def borrow_book(self, book_id):
    """
    Marca un libro como prestado en la base de datos según el ID del libro dado.
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.borrow_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE books SET borrowed = 1 WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()