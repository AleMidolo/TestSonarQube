def add_item(self, item, price, quantity=1):
    """
    Agrega información del artículo a los elementos de la lista de compras, incluyendo precio y cantidad. La cantidad predeterminada es 1
    :param item: string, Artículo a ser agregado
    :param price: float, El precio del artículo
    :param quantity:int, El número de artículos, predeterminado a 1
    :return:None
    >>> shoppingcart = ShoppingCart()
    >>> shoppingcart.add_item("apple", 1, 5)
    self.items = {"apple":{"price":1, "quantity":5}}
    """
    if not hasattr(self, 'items'):
        self.items = {}
    
    self.items[item] = {"price": price, "quantity": quantity}