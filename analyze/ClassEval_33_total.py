def total(self):
    """
        Calcular el costo total de los artículos en el carrito.
        :return: float, costo total de los artículos
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.total()
        329.0

        """
    total_cost = 0
    for item in self.cart:
        total_cost += item['quantity'] * item['price']
    return total_cost