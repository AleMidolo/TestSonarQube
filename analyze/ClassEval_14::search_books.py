def search_books(self):
    """
        从数据库中检索所有书籍并返回其信息。
        :return books: list[tuple], 数据库中所有书籍的信息
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
    self.cursor.execute('SELECT * FROM books')
    books = self.cursor.fetchall()
    return books