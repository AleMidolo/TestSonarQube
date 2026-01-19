def restock_item(self, item_name, quantity):
    """
    एक उत्पाद के इन्वेंटरी को फिर से भरता है जो पहले से वेंडिंग मशीन में है।
    :param item_name: उत्पाद का नाम जिसे फिर से भरा जाना है, str.
    :param quantity: उत्पाद की मात्रा जिसे फिर से भरा जाना है, int.
    :return: यदि उत्पाद पहले से वेंडिंग मशीन में है, तो True लौटाता है, अन्यथा, False लौटाता है।
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