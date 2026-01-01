def remove_book(self, title, quantity):
    """
        Remove one or several books from inventory which is sorted by book title.
        Raise an error for invalid input.
        :param title: str, the book title
        :param quantity: int
        """
    if title not in self.inventory:
        raise ValueError('Book not found in inventory.')
    if quantity <= 0:
        raise ValueError('Quantity must be greater than zero.')
    if self.inventory[title] < quantity:
        raise ValueError('Not enough books in inventory to remove.')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]