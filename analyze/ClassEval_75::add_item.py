def add_item(self, item, price, quantity=1):
    """
        Add item information to the shopping list, including price and quantity. Default quantity is 1
        :param item: string, item to be added
        :param price: float, price of the item
        :param quantity:int, number of items, default is 1
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.view_items()
        {"apple":{"price":1, "quantity":5}}
        """
    if item in self.items:
        self.items[item]['quantity'] += quantity
    else:
        self.items[item] = {'price': price, 'quantity': quantity}