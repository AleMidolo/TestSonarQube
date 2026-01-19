def add_product(self, product_id, name, quantity):
    """
    Agrega un producto al inventario y suma la cantidad si ya existía en el inventario.
    O simplemente agrega un nuevo producto al diccionario en caso contrario.
    :param product_id: int
    :param name: str, nombre del producto
    :param quantity: int, cantidad del producto
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.inventory
    {1: {'name': 'product1', 'quantity': 3}}
    """
    if product_id in self.inventory:
        self.inventory[product_id]['quantity'] += quantity
    else:
        self.inventory[product_id] = {'name': name, 'quantity': quantity}