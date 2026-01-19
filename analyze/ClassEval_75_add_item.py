def add_item(self, item, price, quantity=1):
    """
    将商品信息添加到购物清单中,包括价格和数量。默认数量为1
    :param item: string, 要添加的商品
    :param price: float, 商品的价格
    :param quantity:int, 商品的数量,默认为1
    :return: None
    >>> shoppingcart = ShoppingCart()
    >>> shoppingcart.add_item("apple", 1, 5)
    self.items = {"apple":{"price":1, "quantity":5}}
    """
    if not hasattr(self, 'items'):
        self.items = {}
    
    self.items[item] = {"price": price, "quantity": quantity}