def total_price(self) -> float:
    """
        计算购物清单中所有商品的总价格，即每种商品的数量乘以价格
        :return: float，购物清单中所有商品的总价格
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.add_item("banana", 2, 3)
        >>> shoppingcart.total_price()
        11.0
        """
    total = 0.0
    for item_info in self.items.values():
        total += item_info['price'] * item_info['quantity']
    return total