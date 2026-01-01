def remove_book(self, title, quantity):
    """
        इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
        अमान्य इनपुट मिलने पर झूठा उठाएं।
        :param title: str, किताब का शीर्षक
        :param quantity: int
        """
    if not isinstance(title, str):
        raise ValueError('Title must be a string')
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Quantity must be a positive integer')
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    if self.inventory[title] < quantity:
        raise ValueError(f"Cannot remove {quantity} copies of '{title}'. Only {self.inventory[title]} available")
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]