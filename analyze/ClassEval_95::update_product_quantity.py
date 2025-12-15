def update_product_quantity(self, product_id, quantity):
        """
        根据 product_id，将数量添加到库存中对应的产品。
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """
        if product_id in self.inventory:
            self.inventory[product_id]['quantity'] += quantity