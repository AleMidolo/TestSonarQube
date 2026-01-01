def remove_item(self, item, quantity=1):
    """
        Reduce the specified quantity from the item in the shopping list
        :param item:string, The item to reduce
        :param quantity:int, The quantity to reduce
        :return:None
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        self.items = {"apple":{"price":1, "quantity":2}}
        """
    if item in self.items:
        if self.items[item]['quantity'] > quantity:
            self.items[item]['quantity'] -= quantity
        elif self.items[item]['quantity'] == quantity:
            del self.items[item]