def remove_book(self, title, quantity):
    """
        Remove one or several books from inventory which is sorted by book title.
        Raise false while get invalid input.
        :param title: str, the book title
        :param quantity: int
        """
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Quantity must be a positive integer')
    if quantity > self.inventory[title]:
        raise ValueError(f"Cannot remove {quantity} copies of '{title}'. Only {self.inventory[title]} available")
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]