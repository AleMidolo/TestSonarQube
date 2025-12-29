def view_inventory(self):
    """
        Ottieni l'inventario della Gestione Libri.
        :return self.inventory: dizionario, {titolo(str): quantità(int), ...}
        >>> bookManagement = BookManagement()
        >>> bookManagement.add_book("book1", 1)
        >>> bookManagement.add_book("book2", 1)
        >>> bookManagement.view_inventory()
        {'book1': 1, 'book2': 1}
        """
    return self.inventory