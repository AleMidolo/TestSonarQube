def add_book(self, title, quantity=1):
    """
        Aggiungi uno o più libri all'inventario che è ordinato per titolo del libro.
        :param title: str, il titolo del libro
        :param quantity: int, il valore predefinito è 1.
        """
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity