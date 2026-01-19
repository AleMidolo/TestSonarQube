def get_product_quantity(self, product_id):
    """
    Obtiene la cantidad de un producto específico por product_id.
    :param product_id: int
    :return: si el product_id está en inventario, entonces devuelve la cantidad correspondiente,
            o False en caso contrario.
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.get_product_quantity(1)
    3
    >>> warehouse.get_product_quantity(2)
    False
    """
    if product_id in self.inventory:
        return self.inventory[product_id]['quantity']
    return False