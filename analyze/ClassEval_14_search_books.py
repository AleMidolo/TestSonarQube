def search_books(self):
    """
    Retrieves all books from the database and returns their information.
    :return books: list[tuple], the information of all books in database
    >>> book_db.search_books()
    [(1, 'book1', 'author', 1)]
    """
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return books