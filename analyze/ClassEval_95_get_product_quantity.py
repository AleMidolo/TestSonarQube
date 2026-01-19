def get_product_quantity(self, product_id):
    """
    根据 product_id 获取特定产品的数量。
    :param product_id, int
    :return: 如果 product_id 在库存中，则返回相应的数量，
            否则返回 False。
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.get_product_quantity(1)
    3
    >>> warehouse.get_product_quantity(2)
    False
    """
    if product_id in self.inventory:
        return self.inventory[product_id]['quantity']
    else:
        return False