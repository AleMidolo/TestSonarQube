def add_book(self, title, author):
    """
    Agrega un libro a la base de datos con el título y autor especificados, 
    estableciendo su disponibilidad a 1 como libre para prestar.
    :param title: str, título del libro
    :param author: str, nombre del autor
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    >>> book_db.add_book('book1', 'author')
    """
    self.cursor.execute('\n            INSERT INTO books (title, author, available) VALUES (?, ?, 1)\n        ', (title, author))
    self.connection.commit()