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
    if not hasattr(self, 'inventory'):
        self.inventory = []
    
    for book in self.inventory:
        if book.get('title') == title:
            current_quantity = book.get('quantity', 0)
            
            # Si la cantidad a eliminar es mayor o igual a la existente, eliminar el libro
            if quantity >= current_quantity:
                self.inventory.remove(book)
            else:
                # Reducir la cantidad
                book['quantity'] = current_quantity - quantity
            
            return True
    
    # Si no se encuentra el libro
    return False