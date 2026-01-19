def display_items(self):
    """
    Muestra los productos en la máquina expendedora.
    :return: Si la máquina expendedora está vacía, devuelve False, de lo contrario, devuelve una lista de los productos en la máquina expendedora, str.
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.display_items()
    False
    >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
    >>> vendingMachine.display_items()
    'Coke - $1.25 [10]'

    """
    if not self.inventory:
        return False
    
    items = []
    for item_name, item_info in self.inventory.items():
        price = item_info['price']
        quantity = item_info['quantity']
        items.append(f"{item_name} - ${price} [{quantity}]")
    
    return '\n'.join(items)