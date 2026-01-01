def view_book_quantity(self, title):
    """
        Obtener la cantidad de un libro.
        :param title: str, el título del libro.
        :return quantity: la cantidad de este título de libro. devuelve 0 cuando el título no existe en self.inventory
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.view_book_quantity("book3")
        0
        """
    return self.inventory.get(title, 0)