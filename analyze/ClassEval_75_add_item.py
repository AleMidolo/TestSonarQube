def add_item(self, item, price, quantity=1):
    """
        Add item information to the shopping list items, including price and quantity. The default quantity is 1
        :param item: string, Item to be added
        :param price: float, The price of the item
        :param quantity:int, The number of items, defaults to 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        self.items = {"apple":{"price":1, "quantity":5}}
        """
    if item in self.items:
        self.items[item]['quantity'] += quantity
    else:
        self.items[item] = {'price': price, 'quantity': quantity}