def update_product_quantity(self, product_id, quantity):
    """
        product_id के अनुसार, इन्वेंटरी में संबंधित उत्पाद की मात्रा में जोड़ें।
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.update_product_quantity(1, -1)
        >>> warehouse.inventory
        {1: {'name': 'product1', 'quantity': 2}}
        """
    if product_id in self.inventory:
        self.inventory[product_id]['quantity'] += quantity