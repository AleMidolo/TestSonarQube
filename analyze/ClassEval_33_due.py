def due(self):
    """
    Calcola l'importo finale da pagare dopo aver applicato lo sconto.
    :return: float, importo finale da pagare
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    >>> ds.due()
    312.55

    """
    total = sum(item['quantity'] * item['price'] for item in self.cart)
    discount = self.promotion(self) if self.promotion else 0
    return round(total - discount, 2)