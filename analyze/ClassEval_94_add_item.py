def add_item(self, item_name, price, quantity):
    """
    वेंडिंग मशीन के इन्वेंटरी में एक उत्पाद जोड़ता है।
    :param item_name: जो उत्पाद जोड़ा जाना है उसका नाम, str.
    :param price: जो उत्पाद जोड़ा जाना है उसकी कीमत, float.
    :param quantity: जो उत्पाद जोड़ा जाना है उसकी मात्रा, int.
    :return: None
    >>> vendingMachine = VendingMachine()
    >>> vendingMachine.add_item('Coke', 1.25, 10)
    >>> vendingMachine.inventory
    {'Coke': {'price': 1.25, 'quantity': 10}}

    """
    self.inventory[item_name] = {'price': price, 'quantity': quantity}