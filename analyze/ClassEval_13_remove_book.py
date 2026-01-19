def remove_book(self, title, quantity):
    """
    Remove one or several books from inventory which is sorted by book title.
    Raise false while get invalid input.
    :param title: str, the book title
    :param quantity: int
    """
    if not isinstance(title, str) or not isinstance(quantity, int):
        raise ValueError("Invalid input")
    
    if quantity <= 0:
        raise ValueError("Invalid input")
    
    if not hasattr(self, 'inventory'):
        self.inventory = {}
    
    if title not in self.inventory:
        raise ValueError("Invalid input")
    
    if self.inventory[title] < quantity:
        raise ValueError("Invalid input")
    
    self.inventory[title] -= quantity
    
    if self.inventory[title] == 0:
        del self.inventory[title]