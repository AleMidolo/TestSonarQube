def track_order(self, order_id):
    """
        विशिष्ट आदेश की स्थिति प्राप्त करें।
        :param order_id: int
        :return False: केवल तभी यदि order_id self.orders में नहीं है।
        >>> warehouse.add_product(1, "product1", 3)
        >>> warehouse.create_order(1, 1, 2)
        >>> warehouse.track_order(1)
        'Shipped'
        """
    if order_id in self.orders:
        return self.orders[order_id]['status']
    else:
        return False