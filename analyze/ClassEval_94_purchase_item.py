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
    # Verifica se il prodotto esiste nell'inventario
    if item_name not in self.inventory:
        return False
    
    # Ottieni le informazioni del prodotto
    item = self.inventory[item_name]
    price = item['price']
    quantity = item['quantity']
    
    # Verifica se il prodotto è disponibile (quantità > 0)
    if quantity <= 0:
        return False
    
    # Verifica se il saldo è sufficiente per l'acquisto
    if self.balance < price:
        return False
    
    # Effettua l'acquisto
    self.balance -= price
    self.inventory[item_name]['quantity'] -= 1
    
    return self.balance