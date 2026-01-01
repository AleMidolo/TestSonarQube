def track_order(self, order_id):
    """
        Obtener el estado de un pedido específico.
        :param order_id: int
        :return False: solo si el order_id no está en self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Enviado'
        """
    if order_id in self.orders:
        return self.orders[order_id]['status']
    else:
        return False