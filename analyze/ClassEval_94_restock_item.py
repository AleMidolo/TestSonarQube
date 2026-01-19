def restock_item(self, item_name, quantity):
    """
        Reabastece el inventario de un producto que ya está en la máquina expendedora.
        :param item_name: El nombre del producto a reabastecer, str.
        :param quantity: La cantidad del producto a reabastecer, int.
        :return: Si el producto ya está en la máquina expendedora, devuelve True, de lo contrario, devuelve False.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
        >>> vendingMachine.restock_item('Coke', 10)
        True
        >>> vendingMachine.restock_item('Pizza', 10)
        False
        """
    if item_name in self.inventory:
        self.inventory[item_name]['quantity'] += quantity
        return True
    else:
        return False