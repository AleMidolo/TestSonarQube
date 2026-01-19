def add_item(self, item_name, price, quantity):
    """
    Adds a product to the vending machine's inventory.
    :param item_name: The name of the product to be added, str.
    :param price: The price of the product to be added, float.
    :param quantity: The quantity of the product to be added, int.
    :return: None
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.add_item('Coke', 1.25, 10)
    >>> vendingMachine.inventory
    {'Coke': {'price': 1.25, 'quantity': 10}}

    """
    self.inventory[item_name] = {'price': price, 'quantity': quantity}