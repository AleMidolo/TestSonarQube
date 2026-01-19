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
    
    # Cerca il libro nell'inventario
    found = False
    for book in self.inventory:
        if book['title'] == title:
            found = True
            if book['quantity'] < quantity:
                raise ValueError(f"Quantità insufficiente. Disponibili: {book['quantity']}, richiesti: {quantity}")
            
            book['quantity'] -= quantity
            
            # Se la quantità diventa 0, rimuovi il libro dall'inventario
            if book['quantity'] == 0:
                self.inventory.remove(book)
            
            break
    
    if not found:
        raise ValueError(f"Libro '{title}' non trovato nell'inventario")