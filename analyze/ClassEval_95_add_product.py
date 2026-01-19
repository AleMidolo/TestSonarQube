def add_product(self, product_id, name, quantity):
    """
    将产品添加到库存，如果它已经存在于库存中，则增加数量。
    否则，直接将新产品添加到字典中。
    :param product_id: int
    :param name: str, 产品名称
    :param quantity: int, 产品数量
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.inventory
    {1: {'name': 'product1', 'quantity': 3}}
    """
    if product_id in self.inventory:
        self.inventory[product_id]['quantity'] += quantity
    else:
        self.inventory[product_id] = {'name': name, 'quantity': quantity}