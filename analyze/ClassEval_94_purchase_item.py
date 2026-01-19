def purchase_item(self, item_name):
    """
    Compra un producto de la máquina expendedora y devuelve el saldo después de la compra y muestra "compra no exitosa" si el producto está agotado.
    :param item_name: El nombre del producto a comprar, str.
    :return: Si es exitoso, devuelve el saldo de la máquina expendedora después de que se compra el producto, float; de lo contrario, devuelve False.
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
    
    item = self.inventory[item_name]
    
    # Check if item is in stock
    if item['quantity'] <= 0:
        print("compra no exitosa")
        return False
    
    # Check if balance is sufficient
    if self.balance < item['price']:
        return False
    
    # Process the purchase
    self.balance -= item['price']
    item['quantity'] -= 1
    
    return self.balance