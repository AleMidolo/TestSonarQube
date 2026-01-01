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
    return ' '.join((f"{item} - ${data['price']} [{data['quantity']}]" for item, data in self.inventory.items()))