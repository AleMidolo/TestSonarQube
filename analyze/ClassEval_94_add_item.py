def add_item(self, item_name, price, quantity):
    """
        Agrega un producto al inventario de la máquina expendedora.
        :param item_name: El nombre del producto a agregar, str.
        :param price: El precio del producto a agregar, float.
        :param quantity: La cantidad del producto a agregar, int.
        :return: None
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.add_item('Coke', 1.25, 10)
        >>> vendingMachine.inventory
        {'Coke': {'price': 1.25, 'quantity': 10}}
        """
    self.inventory[item_name] = {'price': price, 'quantity': quantity}