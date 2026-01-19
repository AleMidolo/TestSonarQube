def remove_item(self, item, quantity=1):
    """
        Resta la cantidad especificada del artículo de los elementos de la lista de compras
        :param item:string, Artículo que se va a restar en cantidad
        :param quantity:int, Cantidad a restar
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