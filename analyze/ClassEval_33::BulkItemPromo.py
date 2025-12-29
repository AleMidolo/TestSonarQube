@staticmethod
def BulkItemPromo(order):
    """
        Calculate the discount based on bulk item quantity in the order.In the same order, if the quantity of a single item reaches 20 or more, each item will enjoy a 10% discount.
        :param order: object, the order to apply the discount to
        :return: float, discount amount
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        >>> DiscountStrategy.BulkItemPromo(order)
        47.0

        """
    discount = 0
    for item in order.cart:
        if item['quantity'] >= 20:
            discount += item['quantity'] * item['price'] * 0.1
    return discount