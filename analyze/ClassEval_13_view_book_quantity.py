def view_book_quantity(self, title):
    """
    Restituisce il numero di copie di un libro.
    :param title: str, il titolo del libro.
    :return quantity: la quantità di questo titolo di libro. restituisce 0 quando il titolo non esiste in self.invenroty
    >>> bookManagement = BookManagement()
    >>> bookManagement.add_book("book1", 1)
    >>> bookManagement.view_book_quantity("book3")
    0
    """
    return self.inventory.get(title, 0)