@staticmethod
def LargeOrderPromo(order):
    """
        Calculate the discount based on the number of different products in the order.If the quantity of different products in the order reaches 10 or more, the entire order will enjoy a 7% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
    discount = 0
    if len(order.cart) >= 10:
        discount = order.total() * 0.07
    return discount