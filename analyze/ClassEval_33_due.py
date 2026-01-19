def due(self):
    """
    Calcular el monto final a pagar después de aplicar el descuento.
    :return: float, monto final a pagar
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    >>> ds.due()
    312.55

    """
    total = sum(item['quantity'] * item['price'] for item in self.cart)
    discount = self.promotion(self)
    return round(total - discount, 2)