@staticmethod
def FidelityPromo(order):
    """
        Calcula el descuento basado en los puntos de fidelidad del cliente. Los clientes con más de 1000 puntos pueden disfrutar de un 5% de descuento en todo el pedido.
        :param order: objeto, el pedido al que se aplicará el descuento
        :return: float, monto del descuento
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """
    if order.customer.get('fidelity', 0) > 1000:
        return order.total() * 0.05
    return 0.0