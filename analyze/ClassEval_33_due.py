def due(self):
    """
    Calculate the final amount to be paid after applying the discount.
    :return: float, final amount to be paid
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> ds = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    >>> ds.due()
    312.55

    """
    total = sum(item['quantity'] * item['price'] for item in self.cart)
    discount = self.promotion(self) if self.promotion else 0
    return round(total - discount, 2)