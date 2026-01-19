@staticmethod
def BulkItemPromo(order):
    """
    Calcola lo sconto basato sulla quantità di articoli in blocco nell'ordine. Nello stesso ordine, se la quantità di un singolo articolo raggiunge 20 o più, ogni articolo godrà di uno sconto del 10%.
    :param order: oggetto, l'ordine a cui applicare lo sconto
    :return: float, importo dello sconto
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
    >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
    >>> DiscountStrategy.BulkItemPromo(order)
    47.0

    """
    discount = 0
    for item in order.cart:
        if item['quantity'] >= 20:
            discount += item['quantity'] * item['price'] * 0.10
    return discount