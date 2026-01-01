def create_order(self, order_id, product_id, quantity):
    """
    Crea un ordine che include le informazioni del prodotto, come id e quantità.
    E inserisce il nuovo ordine in self.orders.
    Il valore predefinito dello stato è 'Spedito'.
    :param order_id: int
    :param product_id: int
    :param quantity: la quantità di prodotto che è stata selezionata.
    :return False: solo se product_id non è presente nell'inventario o la quantità non è adeguata
    >>> warehouse.add_product(1, "product1", 3)
    >>> warehouse.create_order(1, 1, 2)
    >>> warehouse.orders
    {1: {'product_id': 1, 'quantity': 2, 'status': 'Spedito'}}
    >>> warehouse.create_order(1, 2, 2)
    False
    """
    if product_id in self.inventory and self.inventory[product_id]['quantity'] >= quantity:
        self.orders[order_id] = {'product_id': product_id, 'quantity': quantity, 'status': 'Spedito'}
        self.inventory[product_id]['quantity'] -= quantity
    else:
        return False