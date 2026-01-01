def change_order_status(self, order_id, status):
    """
        यदि इनपुट order_id self.orders में है तो ऑर्डर का स्टेटस बदलें।
        :param order_id: int
        :param status: str, वह स्थिति जिसमें परिवर्तन किया जाएगा
        :return False: केवल तभी यदि order_id self.orders में नहीं है
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