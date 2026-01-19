@staticmethod
def FidelityPromo(order):
    """
    Calculate the discount based on the fidelity points of the customer.Customers with over 1000 points can enjoy a 5% discount on the entire order.
    :param order: object, the order to apply the discount to
    :return: float, discount amount
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
    >>> DiscountStrategy.FidelityPromo(order)
    16.45

    """
    if order.customer['fidelity'] > 1000:
        return order.total() * 0.05
    return 0.0