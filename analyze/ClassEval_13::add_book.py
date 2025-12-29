def add_book(self, title, quantity=1):
    """
        Add one or several books to inventory which is sorted by book title.
        :param title: str, the book title
        :param quantity: int, default value is 1.
        """
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity