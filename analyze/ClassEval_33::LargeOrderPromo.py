@staticmethod
def LargeOrderPromo(order):
    """
        Calcola lo sconto basato sul numero di prodotti diversi nell'ordine. Se la quantità di prodotti diversi nell'ordine raggiunge 10 o più, l'intero ordine godrà di uno sconto del 7%.
        :param order: oggetto, l'ordine a cui applicare lo sconto
        :return: float, importo dello sconto
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
    unique_products = len({item['product'] for item in order.cart})
    return order.total() * 0.07 if unique_products >= 10 else 0