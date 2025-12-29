def remove_book(self, title, quantity):
    """
        Remove one or several books from inventory which is sorted by book title.
        Raise an error on invalid input.
        :param title: str, the book title
        :param quantity: int
        """
    if title not in self.inventory or quantity <= 0:
        raise ValueError('Invalid input')
    if self.inventory[title] < quantity:
        raise ValueError('Not enough books in inventory')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]