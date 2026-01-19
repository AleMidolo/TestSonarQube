def purchase_item(self, item_name):
    """
    从自动售货机购买产品，并在购买后返回余额，如果产品缺货则显示购买失败。
    :param item_name: 要购买的产品名称，str。
    :return: 如果成功，返回购买后自动售货机的余额，float；否则，返回 False。
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
    
    # Check if item is in stock
    if self.inventory[item_name]['quantity'] <= 0:
        return False
    
    # Get item price
    item_price = self.inventory[item_name]['price']
    
    # Check if balance is sufficient
    if self.balance < item_price:
        return False
    
    # Process purchase
    self.balance -= item_price
    self.inventory[item_name]['quantity'] -= 1
    
    return self.balance