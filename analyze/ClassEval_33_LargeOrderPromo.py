@staticmethod
def LargeOrderPromo(order):
    """
    根据订单中不同产品的数量计算折扣。如果订单中不同产品的数量达到10个或更多，则整个订单享受7%的折扣。
    :param order: object, 要应用折扣的订单
    :return: float, 折扣金额
    >>> customer = {'name': 'John Doe', 'fidelity': 1200}
    >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
    >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
    >>> DiscountStrategy.LargeOrderPromo(order)
    0.0

    """
    # 计算订单中不同产品的数量（即购物车中的项目数）
    distinct_items = len(order.cart)
    
    # 如果不同产品的数量达到10个或更多，则整个订单享受7%的折扣
    if distinct_items >= 10:
        return order.total() * 0.07
    
    return 0.0