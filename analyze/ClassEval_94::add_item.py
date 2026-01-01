def add_item(self, item_name, price, quantity):
    """
        将产品添加到自动售货机的库存中。
        :param item_name: 要添加的产品名称，str。
        :param price: 要添加的产品价格，float。
        :param quantity: 要添加的产品数量，int。
        :return: None
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.add_item('Coke', 1.25, 10)
        >>> vendingMachine.inventory
        {'Coke': {'price': 1.25, 'quantity': 10}}

        """
    if item_name not in self.inventory:
        self.inventory[item_name] = {'price': price, 'quantity': quantity}
    else:
        self.inventory[item_name]['quantity'] += quantity