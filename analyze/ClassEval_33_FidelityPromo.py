@staticmethod
def FidelityPromo(order):
    """
        根据客户的忠诚度积分计算折扣。积分超过1000的客户可以享受整个订单5%的折扣。
        :param order: object, 要应用折扣的订单
        :return: float, 折扣金额
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.FidelityPromo)
        >>> DiscountStrategy.FidelityPromo(order)
        16.45

        """
    return order.total() * 0.05 if order.customer['fidelity'] >= 1000 else 0