@staticmethod
def LargeOrderPromo(order):
    """
        Calcula el descuento basado en la cantidad de productos diferentes en el pedido. Si la cantidad de productos diferentes en el pedido alcanza 10 o más, todo el pedido disfrutará de un descuento del 7%.
        :param order: objeto, el pedido al que se aplicará el descuento
        :return: float, monto del descuento
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
    unique_products = len(set((item['product'] for item in order.cart)))
    return order.total() * 0.07 if unique_products >= 10 else 0