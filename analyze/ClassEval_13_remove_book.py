def remove_book(self, title, quantity):
    """
        इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
        अमान्य इनपुट मिलने पर झूठा उठाएं।
        :param title: str, किताब का शीर्षक
        :param quantity: int
        """
    if title not in self.inventory or quantity <= 0:
        raise ValueError('Invalid input')
    if self.inventory[title] < quantity:
        raise ValueError('Not enough books in inventory')
    self.inventory[title] -= quantity
    if self.inventory[title] == 0:
        del self.inventory[title]