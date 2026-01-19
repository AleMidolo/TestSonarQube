def search_books(self):
    """
    डेटाबेस से सभी किताबों को प्राप्त करता है और उनकी जानकारी लौटाता है।
    :return books: list[tuple], डेटाबेस में सभी किताबों की जानकारी
    >>> book_db.search_books()
    [(1, 'book1', 'author', 1)]
    """
    cursor = self.connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    return books