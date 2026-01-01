def add_book(self, title, quantity=1):
    """
        将一本或多本书添加到按书名排序的库存中。
        :param title: str，书名
        :param quantity: int，默认值为1。
        """
    if not isinstance(title, str) or not isinstance(quantity, int) or quantity <= 0:
        raise False
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity