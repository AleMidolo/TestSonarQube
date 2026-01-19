@staticmethod
def BulkItemPromo(order):
    """
    根据订单中的大宗商品数量计算折扣。在同一订单中，如果单个商品的数量达到20个或更多，每个商品将享受10%的折扣。
    :param order: object, 要应用折扣的订单
    :return: float, 折扣金额
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