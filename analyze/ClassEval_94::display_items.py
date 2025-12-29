def display_items(self):
    """
        वेंडिंग मशीन में उत्पादों को प्रदर्शित करता है।
        :return: यदि वेंडिंग मशीन खाली है, तो False लौटाता है, अन्यथा, वेंडिंग मशीन में उत्पादों की एक सूची लौटाता है, str।
        >>> vendingMachine = VendingMachine()
        >>> vendingMachine.display_items()
        False
        >>> vendingMachine.inventory = {'Coke': {'price': 1.25, 'quantity': 10} }
        >>> vendingMachine.display_items()
        'Coke - $1.25 [10]'

        """
    if not self.inventory:
        return False
    items_display = []
    for item_name, details in self.inventory.items():
        price = details['price']
        quantity = details['quantity']
        items_display.append(f'{item_name} - ${price} [{quantity}]')
    return '\n'.join(items_display)