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
    found = False
    
    # Assumendo che self.inventory sia un dizionario con titolo come chiave
    if hasattr(self, 'inventory'):
        if title in self.inventory:
            if self.inventory[title] < quantity:
                raise ValueError(f"Quantità insufficiente. Disponibili: {self.inventory[title]}, richiesti: {quantity}")
            
            self.inventory[title] -= quantity
            
            # Rimuovi completamente il libro se la quantità diventa 0
            if self.inventory[title] == 0:
                del self.inventory[title]
            
            found = True
        else:
            raise KeyError(f"Il libro '{title}' non è presente nell'inventario")
    else:
        raise AttributeError("L'inventario non è stato inizializzato")