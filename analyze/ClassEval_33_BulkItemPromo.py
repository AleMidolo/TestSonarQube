@staticmethod
def BulkItemPromo(order):
    """
        Calcula el descuento basado en la cantidad de artículos al por mayor en el pedido. En el mismo pedido, si la cantidad de un solo artículo alcanza 20 o más, cada artículo disfrutará de un descuento del 10%.
        :param order: objeto, el pedido al que se aplicará el descuento
        :return: float, monto del descuento
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        >>> DiscountStrategy.BulkItemPromo(order)
        47.0

        """
    return sum((item['quantity'] * item['price'] * 0.1 for item in order.cart if item['quantity'] >= 20))