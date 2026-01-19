def add_book(self, title, quantity=1):
    """
    एक या एक से अधिक किताबों को इन्वेंटरी में जोड़ें जो किताब के शीर्षक के अनुसार क्रमबद्ध है।
    :param title: str, किताब का शीर्षक
    :param quantity: int, डिफ़ॉल्ट मान 1 है।
    """
    if title in self.inventory:
        self.inventory[title] += quantity
    else:
        self.inventory[title] = quantity
    
    # Sort the inventory by book title
    self.inventory = dict(sorted(self.inventory.items()))