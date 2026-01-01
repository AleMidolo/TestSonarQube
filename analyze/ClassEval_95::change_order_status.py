def change_order_status(self, order_id, status):
    """
        Cambia el estado del pedido si el order_id de entrada está en self.orders.
        :param order_id: int
        :param status: str, el estado al que se va a cambiar
        :return False: solo si el order_id no está en self.orders
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