def remove_book(self, book_id):
    """
    根据给定的书籍ID从数据库中移除一本书。
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