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
    if item_name in self.inventory and self.inventory[item_name]['quantity'] > 0:
        if self.balance >= self.inventory[item_name]['price']:
            self.balance -= self.inventory[item_name]['price']
            self.inventory[item_name]['quantity'] -= 1
            return self.balance
        else:
            return False
    else:
        return False