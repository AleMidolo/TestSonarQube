def add_item(self, item, price, quantity=1):
    """
        Aggiungi informazioni sull'oggetto alla lista della spesa, inclusi prezzo e quantità. La quantità predefinita è 1
        :param item: stringa, Oggetto da aggiungere
        :param price: float, Il prezzo dell'oggetto
        :param quantity:int, Il numero di oggetti, predefinito a 1
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