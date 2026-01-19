def track_order(self, order_id):
    """
        Ottieni lo stato di un ordine specifico.
        :param order_id: int
        :return False: solo se l'order_id non è presente in self.orders.
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Spedito'
        """
    if order_id in self.orders:
        return self.orders[order_id]['status']
    else:
        return False