def remove_book(self, title, quantity):
    """
        从按书名排序的库存中移除一本或多本书籍。
        如果输入无效则引发错误。
        :param title: str，书名
        :param quantity: int
        """
    if not isinstance(title, str):
        raise TypeError('Title must be a string')
    if not isinstance(quantity, int):
        raise TypeError('Quantity must be an integer')
    if quantity <= 0:
        raise ValueError('Quantity must be positive')
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    current_quantity = self.inventory[title]
    if quantity > current_quantity:
        raise ValueError(f"Cannot remove {quantity} copies of '{title}'. Only {current_quantity} available")
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]