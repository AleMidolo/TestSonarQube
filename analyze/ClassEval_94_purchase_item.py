def purchase_item(self, item_name):
    """
    Acquista un prodotto dal distributore automatico e restituisce il saldo dopo l'acquisto e visualizza acquisto non riuscito se il prodotto è esaurito.
    :param item_name: Il nome del prodotto da acquistare, str.
    :return: Se riuscito, restituisce il saldo del distributore automatico dopo l'acquisto del prodotto, float, altrimenti, restituisce False.
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
    
    # Process purchase
    self.balance -= item['price']
    item['quantity'] -= 1
    
    return self.balance