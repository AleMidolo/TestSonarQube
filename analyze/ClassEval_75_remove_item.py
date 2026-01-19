def remove_item(self, item, quantity=1):
    """
    从购物清单中减去指定数量的物品
    :param item:string, 要减去数量的物品
    :param quantity:int, 要减去的数量
    :return:None
    >>> shoppingcart.add_item("apple", 1, 5)
    >>> shoppingcart.remove_item("apple", 3)
    self.items = {"apple":{"price":1, "quantity":2}}
    """
    if item in self.items:
        self.items[item]["quantity"] -= quantity
        if self.items[item]["quantity"] <= 0:
            del self.items[item]