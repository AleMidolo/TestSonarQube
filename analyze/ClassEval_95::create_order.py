def create_order(self, order_id, product_id, quantity):
    """
        创建一个订单，其中包含产品的信息，如ID和数量。
        并将新订单放入self.orders中。
        状态的默认值为'Shipped'。
        :param order_id: int
        :param product_id: int
        :param quantity: 被选择的产品数量。
        :return False: 仅当product_id不在库存中或数量不足时
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """
    if product_id not in self.inventory:
        return False
    if self.inventory[product_id]['quantity'] < quantity:
        return False
    self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
    self.inventory[product_id]['quantity'] -= quantity