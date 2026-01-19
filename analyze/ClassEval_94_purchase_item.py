def purchase_item(self, item_name):
    """
    Purchases a product from the vending machine and returns the balance after the purchase and display purchase unsuccessful if the product is out of stock.
    :param item_name: The name of the product to be purchased, str.
    :return: If successful, returns the balance of the vending machine after the product is purchased, float,otherwise,returns False.
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10}}
    >>> vendingMachine.balance = 1.25
    >>> vendingMachine.purchase_item('Coke')
    0.0
    >>> vendingMachine.purchase_item('Pizza')
    False

    """
    # Check if item exists in inventory
    if item_name not in self.inventory:
        return False
    
    # Get item details
    item = self.inventory[item_name]
    
    # Check if item is in stock
    if item['quantity'] <= 0:
        return False
    
    # Check if balance is sufficient
    if self.balance < item['price']:
        return False
    
    # Process the purchase
    self.balance -= item['price']
    item['quantity'] -= 1
    
    return self.balance