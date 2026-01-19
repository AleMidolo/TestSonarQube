def remove_book(self, title, quantity):
    """
    इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
    अमान्य इनपुट मिलने पर झूठा उठाएं।
    :param title: str, किताब का शीर्षक
    :param quantity: int
    """
    # Validate input
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Invalid title: must be a non-empty string")
    
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Invalid quantity: must be a positive integer")
    
    # Check if book exists in inventory
    if not hasattr(self, 'inventory'):
        self.inventory = {}
    
    if title not in self.inventory:
        raise ValueError(f"Book '{title}' not found in inventory")
    
    # Check if sufficient quantity exists
    if self.inventory[title] < quantity:
        raise ValueError(f"Insufficient quantity: only {self.inventory[title]} available")
    
    # Remove the books
    self.inventory[title] -= quantity
    
    # Remove entry if quantity becomes zero
    if self.inventory[title] == 0:
        del self.inventory[title]
    
    return True