def add_item(self, item_name, price, quantity):
    """
    Aggiunge un prodotto all'inventario del distributore automatico.
    :param item_name: Il nome del prodotto da aggiungere, str.
    :param price: Il prezzo del prodotto da aggiungere, float.
    :param quantity: La quantità del prodotto da aggiungere, int.
    :return: None
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.add_item('Coke', 1.25, 10)
    >>> vendingMachine.inventory
    {'Coke': {'price': 1.25, 'quantity': 10}}

    """
    if not hasattr(self, 'inventory'):
        self.inventory = {}
    
    self.inventory[item_name] = {'price': price, 'quantity': quantity}