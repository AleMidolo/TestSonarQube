def remove_book(self, title, quantity):
    """
        Eliminar uno o varios libros del inventario que está ordenado por título de libro.
        Lanza falso si se recibe una entrada no válida.
        :param title: str, el título del libro
        :param quantity: int
        """
    if title not in self.inventory:
        return False
    if quantity <= 0:
        return False
    if self.inventory[title] < quantity:
        return False
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]
    return True