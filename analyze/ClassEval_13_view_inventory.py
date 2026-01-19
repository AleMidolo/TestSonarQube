def view_inventory(self):
    """
    Obtener el inventario de la Gestión de Libros.
    :return self.inventory: diccionario, {título(str): cantidad(int), ...}
    >>> bookManagement = BookManagement()
    >>> bookManagement.add_book("book1", 1)
    >>> bookManagement.add_book("book2", 1)
    >>> bookManagement.view_inventory()
    {'book1': 1, 'book2': 1}
    """
    return self.inventory