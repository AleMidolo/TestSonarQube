def create_order(self, order_id, product_id, quantity):
    """
        Crear un pedido que incluye la información del producto, como id y cantidad.
        Y poner el nuevo pedido en self.orders.
        El valor predeterminado de estado es 'Shipped'.
        :param order_id: int
        :param product_id: int
        :param quantity: la cantidad de producto que se ha seleccionado.
        :return False: solo si product_id no está en el inventario o la cantidad no es adecuada
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.orders
        {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
        >>> warehouse.create_order(1, 2, 2)
        False
        """
    if product_id not in self.inventory:
        return False
    if quantity <= 0 or quantity > self.inventory[product_id]['quantity']:
        return False
    self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Shipped'}
    return True