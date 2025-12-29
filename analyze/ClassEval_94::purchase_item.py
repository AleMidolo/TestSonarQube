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
    if item_name in self.inventory and self.inventory[item_name]['quantity'] > 0:
        item_price = self.inventory[item_name]['price']
        if self.balance >= item_price:
            self.balance -= item_price
            self.inventory[item_name]['quantity'] -= 1
            return self.balance
        else:
            return False
    return False