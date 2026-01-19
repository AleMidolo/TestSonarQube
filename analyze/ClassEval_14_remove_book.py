def remove_book(self, book_id):
    """
    Elimina un libro de la base de datos según el ID del libro dado.
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