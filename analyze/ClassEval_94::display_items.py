def display_items(self):
    """
        显示自动售货机中的产品。
        :return: 如果自动售货机为空，则返回 False；否则，返回自动售货机中的产品列表，str。
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'
        """
    if not self.inventory:
        return False
    items = []
    for item_name, details in self.inventory.items():
        items.append(f"{item_name} - ${details['price']} [{details['quantity']}]")
    return ', '.join(items)