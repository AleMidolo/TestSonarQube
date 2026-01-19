def add_book(self, title, author):
    """
    Aggiunge un libro al database con il titolo e l'autore specificati, 
    impostando la disponibilità iniziale a 1, quindi libero per il prestito.
    :param title: str, titolo del libro
    :param author: str, nome dell'autore
    >>> book_db = BookManagementDB("test.db")
    >>> book_db.create_table()
    >>> book_db.add_book('book1', 'author')
    """
    cursor = self.conn.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, available) VALUES (?, ?, ?)",
        (title, author, 1)
    )
    self.conn.commit()