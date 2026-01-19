def remove_book(self, title, quantity):
    """
    Rimuovi uno o più libri dall'inventario che è ordinato per titolo del libro.
    Solleva un'eccezione in caso di input non valido.
    :param title: str, il titolo del libro
    :param quantity: int
    """
    if not isinstance(title, str):
        raise TypeError("Il titolo deve essere una stringa")
    
    if not isinstance(quantity, int):
        raise TypeError("La quantità deve essere un intero")
    
    if quantity <= 0:
        raise ValueError("La quantità deve essere maggiore di zero")
    
    if not title.strip():
        raise ValueError("Il titolo non può essere vuoto")
    
    # Cerca il libro nell'inventario (assumendo che self.inventory sia una lista o dizionario)
    # Assumendo che self.inventory sia un dizionario con titolo come chiave
    if not hasattr(self, 'inventory'):
        self.inventory = {}
    
    if title not in self.inventory:
        raise ValueError(f"Il libro '{title}' non è presente nell'inventario")
    
    if self.inventory[title] < quantity:
        raise ValueError(f"Quantità insufficiente. Disponibili: {self.inventory[title]}, richiesti: {quantity}")
    
    self.inventory[title] -= quantity
    
    # Rimuovi il libro dall'inventario se la quantità diventa zero
    if self.inventory[title] == 0:
        del self.inventory[title]