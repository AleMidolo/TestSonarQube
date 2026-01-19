def borrow_book(self, book_id):
    """
    根据给定的书籍ID在数据库中标记一本书为已借出。
    :param book_id: int
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.borrow_book(1)
    """
    import sqlite3
    
    conn = sqlite3.connect(self.db_name)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE books SET is_borrowed = 1 WHERE id = ?", (book_id,))
    
    conn.commit()
    conn.close()