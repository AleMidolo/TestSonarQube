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
    if item_name not in self.inventory:
        return False
    item = self.inventory[item_name]
    if item['quantity'] <= 0:
        print('Acquisto non riuscito: prodotto esaurito')
        return False
    if self.balance < item['price']:
        print('Acquisto non riuscito: saldo insufficiente')
        return False
    self.balance -= item['price']
    item['quantity'] -= 1
    return self.balance