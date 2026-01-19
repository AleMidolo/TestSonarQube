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
    # Count the number of different products in the order
    distinct_products = len(order.cart)
    
    # If there are 10 or more different products, apply 7% discount
    if distinct_products >= 10:
        # Calculate total order amount
        total = sum(item['quantity'] * item['price'] for item in order.cart)
        return total * 0.07
    
    return 0.0