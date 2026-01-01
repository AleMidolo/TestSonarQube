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
    if item_name in self.inventory and self.inventory[item_name]['quantity'] > 0:
        if self.balance >= self.inventory[item_name]['price']:
            self.balance -= self.inventory[item_name]['price']
            self.inventory[item_name]['quantity'] -= 1
            return self.balance
        else:
            return False
    else:
        return False