def add_book(self, title, quantity=1):
    """
        Agrega uno o varios libros al inventario, que está ordenado por el título del libro.
        :param title: str, el título del libro
        :param quantity: int, el valor predeterminado es 1.
        """
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity