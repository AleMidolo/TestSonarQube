def remove_book(self, title, quantity):
    """
        Rimuovi uno o più libri dall'inventario che è ordinato per titolo del libro.
        Solleva un'eccezione in caso di input non valido.
        :param title: str, il titolo del libro
        :param quantity: int
        """
    if title not in self.inventory:
        raise ValueError('Book not found in inventory.')
    if quantity <= 0:
        raise ValueError('Quantity must be greater than zero.')
    if self.inventory[title] < quantity:
        raise ValueError('Not enough copies to remove.')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]