def purchase_item(self, item_name):
    """
    वेंडिंग मशीन से एक उत्पाद खरीदता है और खरीद के बाद शेष राशि लौटाता है और यदि उत्पाद स्टॉक में नहीं है तो खरीद असफल होने का संदेश दिखाता है।
    :param item_name: खरीदने के लिए उत्पाद का नाम, str.
    :return: यदि सफल, तो उत्पाद खरीदने के बाद वेंडिंग मशीन की शेष राशि लौटाता है, float, अन्यथा, False लौटाता है।
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