def remove_book(self, title, quantity):
    """
    Eliminar uno o varios libros del inventario que está ordenado por título de libro.
    Lanza falso si se recibe una entrada no válida.
    :param title: str, el título del libro
    :param quantity: int
    """
    # Validate input
    if not isinstance(title, str) or not isinstance(quantity, int):
        return False
    
    if not title or quantity <= 0:
        return False
    
    # Check if inventory exists
    if not hasattr(self, 'inventory'):
        return False
    
    # Find the book in the inventory
    book_found = False
    for book in self.inventory:
        if book.get('title') == title or (hasattr(book, 'title') and book.title == title):
            book_found = True
            # Get current quantity
            if isinstance(book, dict):
                current_quantity = book.get('quantity', 0)
            else:
                current_quantity = getattr(book, 'quantity', 0)
            
            # Check if we have enough books to remove
            if current_quantity < quantity:
                return False
            
            # Remove the books
            new_quantity = current_quantity - quantity
            
            if isinstance(book, dict):
                if new_quantity == 0:
                    self.inventory.remove(book)
                else:
                    book['quantity'] = new_quantity
            else:
                if new_quantity == 0:
                    self.inventory.remove(book)
                else:
                    book.quantity = new_quantity
            
            return True
    
    # Book not found
    return False