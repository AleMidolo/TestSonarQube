def remove_book(self, title, quantity):
    """
    Eliminar uno o varios libros del inventario que está ordenado por título de libro.
    Lanza falso si se recibe una entrada no válida.
    :param title: str, el título del libro
    :param quantity: int
    """
    # Validar entrada
    if not isinstance(title, str) or not isinstance(quantity, int):
        return False
    
    if not title or quantity <= 0:
        return False
    
    # Buscar el libro en el inventario
    found = False
    for book in self.inventory:
        if book['title'] == title:
            found = True
            # Verificar si hay suficiente cantidad
            if book['quantity'] >= quantity:
                book['quantity'] -= quantity
                # Si la cantidad llega a 0, eliminar el libro del inventario
                if book['quantity'] == 0:
                    self.inventory.remove(book)
                return True
            else:
                # No hay suficiente cantidad
                return False
    
    # Si no se encontró el libro
    if not found:
        return False