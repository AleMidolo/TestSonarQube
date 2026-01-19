def restock_item(self, item_name, quantity):
    """
        补充自动售货机中已存在产品的库存。
        :param item_name: 要补充的产品名称，str。
        :param quantity: 要补充的产品数量，int。
        :return: 如果产品已经在自动售货机中，返回 True；否则，返回 False。
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