def add_item(self, item, price, quantity=1):
    """
        खरीदारी सूची में आइटम की जानकारी जोड़ें, जिसमें कीमत और मात्रा शामिल हैं। डिफ़ॉल्ट मात्रा 1 है
        :param item: string, जोड़ा जाने वाला आइटम
        :param price: float, आइटम की कीमत
        :param quantity:int, आइटम की संख्या, डिफ़ॉल्ट 1 है
        :return:None
        >>> shoppingcart = ShoppingCart()
        >>> shoppingcart.add_item("apple", 1, 5)
        self.items = {"apple":{"price":1, "quantity":5}}
        """
    if item in self.items:
        self.items[item]['quantity'] += quantity
    else:
        self.items[item] = {'price': price, 'quantity': quantity}