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
    items = []
    for item_name, details in self.inventory.items():
        items.append(f"{item_name} - ${details['price']} [{details['quantity']}]")
    return ', '.join(items)