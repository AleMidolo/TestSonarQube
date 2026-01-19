def search_books(self):
    """
        Retrieves all books from the database and returns their information.
        :return books: list[tuple], the information of all books in database
        >>> book_db = BookManagementDB("test.db")
        >>> book_db.add_book('book1', 'author')
        >>> book_db.search_books()
        [(1, 'book1', 'author', 1)]
        """
    self.cursor.execute('SELECT * FROM books')
    return self.cursor.fetchall()