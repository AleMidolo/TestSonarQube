def add_book(self, title, quantity=1):
    """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
    if not isinstance(title, str):
        raise TypeError('Title must be a string')
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Quantity must be a positive integer')
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity