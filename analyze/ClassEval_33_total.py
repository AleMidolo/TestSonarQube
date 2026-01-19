def total(self):
    """
    कार्ट में आइटम्स की कुल लागत की गणना करें।
    :return: float, आइटम्स की कुल लागत
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> ds = DiscountStrategy(customer, cart)
    >>> ds.total()
    329.0

    """
    total_cost = 0.0
    for item in self.cart:
        total_cost += item['quantity'] * item['price']
    return total_cost