def change_order_status(self, order_id, status):
    """
    Cambia lo stato dell'ordine se l'order_id di input è presente in self.orders.
    :param order_id: int
    :param status: str, lo stato a cui si sta cambiando
    :return False: solo se l'order_id non è presente in self.orders
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