def restock_item(self, item_name, quantity):
    """
        Ripristina l'inventario di un prodotto già presente nel distributore automatico.
        :param item_name: Il nome del prodotto da ripristinare, str.
        :param quantity: La quantità del prodotto da ripristinare, int.
        :return: Se il prodotto è già presente nel distributore automatico, restituisce True, altrimenti restituisce False.
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