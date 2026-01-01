def remove_book(self, title, quantity):
    """
        Rimuovi uno o più libri dall'inventario che è ordinato per titolo del libro.
        Solleva un'eccezione in caso di input non valido.
        :param title: str, il titolo del libro
        :param quantity: int
        """
    if not isinstance(title, str):
        raise TypeError('Il titolo deve essere una stringa')
    if not isinstance(quantity, int):
        raise TypeError('La quantità deve essere un intero')
    if quantity <= 0:
        raise ValueError('La quantità deve essere positiva')
    if title not in self.inventory:
        raise ValueError(f"Il libro '{title}' non è presente nell'inventario")
    if self.inventory[title] < quantity:
        raise ValueError(f'Quantità insufficiente. Disponibili: {self.inventory[title]}, Richieste: {quantity}')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]