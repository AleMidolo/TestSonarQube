def remove_book(self, title, quantity):
    """
        इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
        अमान्य इनपुट मिलने पर झूठा उठाएं।
        :param title: str, किताब का शीर्षक
        :param quantity: int
        """
    if not isinstance(title, str) or not isinstance(quantity, int):
        raise ValueError('Invalid input types')
    if quantity <= 0:
        raise ValueError('Quantity must be positive')
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    if self.inventory[title] < quantity:
        raise ValueError(f'Insufficient quantity. Only {self.inventory[title]} copies available')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]