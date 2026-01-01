def remove_book(self, title, quantity):
    """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
    if title not in self.inventory or quantity <= 0:
        raise ValueError('Invalid input: book title does not exist or quantity is invalid.')
    if self.inventory[title] < quantity:
        raise ValueError('Invalid input: not enough books to remove.')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]