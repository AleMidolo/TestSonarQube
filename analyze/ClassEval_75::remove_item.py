def remove_item(self, item, quantity=1):
    """
        Sottrae la quantità specificata dell'elemento dalla lista della spesa
        :param item:string, Elemento da sottrarre in quantità
        :param quantity:int, Quantità da sottrarre
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