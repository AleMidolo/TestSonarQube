def total(self):
    """
        计算购物车中商品的总价格。
        :return: float，商品的总价格
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.total()
        329.0

        """
    return sum((item['quantity'] * item['price'] for item in self.cart))