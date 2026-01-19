def add_book(self, title, quantity=1):
    """
        Agrega uno o varios libros al inventario, que está ordenado por el título del libro.
        :param title: str, el título del libro
        :param quantity: int, el valor predeterminado es 1.
        """
    if not isinstance(title, str) or not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Invalid input: title must be a string and quantity must be a positive integer')
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity