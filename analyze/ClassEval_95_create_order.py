def create_order(self, order_id, product_id, quantity):
    """
    Create a order which includes the infomation of product, like id and quantity.
    And put the new order into self.orders.
    The default value of status is 'Shipped'.
    :param order_id: int
    :param product_id: int
    :param quantity: the quantity of product that be selected.
    :return False: only if product_id is not in inventory or the quantity is not adequate
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.create_order(1, 1, 2)
    >>> warehouse.orders
    {1: {'product_id': 1, 'quantity': 2, 'status': 'Shipped'}}
    >>> warehouse.create_order(1, 2, 2)
    False
    """
    # Check if product_id exists in inventory
    if product_id not in self.inventory:
        return False
    
    # Check if quantity is adequate
    if self.inventory[product_id]['quantity'] < quantity:
        return False
    
    # Create the order
    self.orders[order_id] = {
        'product_id': product_id,
        'quantity': quantity,
        'status': 'Shipped'
    }
    
    # Reduce the inventory quantity
    self.inventory[product_id]['quantity'] -= quantity