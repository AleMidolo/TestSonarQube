def display_items(self):
    """
        Displays the products in the vending machine.
        :return: If the vending machine is empty, returns False, otherwise, returns a list of the products in the vending machine, str.
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'

        """
    if not self.inventory:
        return False
    items_display = []
    for item_name, details in self.inventory.items():
        price = details['price']
        quantity = details['quantity']
        items_display.append(f'{item_name} - ${price} [{quantity}]')
    return '\n'.join(items_display)