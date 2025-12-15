def change_order_status(self, order_id, status):
        """
        如果输入的 order_id 在 self.orders 中，则更改订单状态。
        :param order_id: int
        :param status: str, 要更改为的状态
        :return False: 仅当 order_id 不在 self.orders 中时
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.change_order_status(1, "done")
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'done'}}
        """
        if order_id in self.orders:
            self.orders[order_id]['status'] = status
        else:
            return False