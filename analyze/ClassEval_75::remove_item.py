def remove_item(self, item, quantity=1):
    """
        निर्दिष्ट मात्रा को खरीदारी सूची से आइटम से घटाएं
        :param item:string, घटाने के लिए आइटम
        :param quantity:int, घटाने के लिए मात्रा
        :return:None
        >>> shoppingcart.add_item("apple", 1, 5)
        >>> shoppingcart.remove_item("apple", 3)
        self.items = {"apple":{"price":1, "quantity":2}}
        """
    if item in self.items:
        if self.items[item]['quantity'] > quantity:
            self.items[item]['quantity'] -= quantity
        elif self.items[item]['quantity'] == quantity:
            del self.items[item]