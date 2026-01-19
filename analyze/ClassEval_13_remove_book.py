def remove_book(self, title, quantity):
    """
        从按书名排序的库存中移除一本或多本书籍。
        如果输入无效则引发错误。
        :param title: str，书名
        :param quantity: int
        """
    if title not in self.inventory:
        raise ValueError('Book not found in inventory.')
    if quantity > self.inventory[title]:
        raise ValueError('Not enough quantity to remove.')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]