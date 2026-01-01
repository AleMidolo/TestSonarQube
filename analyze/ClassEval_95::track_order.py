def track_order(self, order_id):
    """
        获取特定订单的状态。
        :param order_id: int
        :return False: 仅当 order_id 不在 self.orders 中时。
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
    if order_id in self.orders:
        return self.orders[order_id]['status']
    else:
        return False