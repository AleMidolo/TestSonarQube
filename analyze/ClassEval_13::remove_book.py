def remove_book(self, title, quantity):
    """
        Rimuovi uno o più libri dall'inventario che è ordinato per titolo del libro.
        Solleva un'eccezione in caso di input non valido.
        :param title: str, il titolo del libro
        :param quantity: int
        """
    if not isinstance(title, str):
        raise TypeError('Title must be a string')
    if not isinstance(quantity, int):
        raise TypeError('Quantity must be an integer')
    if quantity <= 0:
        raise ValueError('Quantity must be positive')
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    if self.inventory[title] < quantity:
        raise ValueError(f"Not enough copies of '{title}' to remove. Available: {self.inventory[title]}, Requested: {quantity}")
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]