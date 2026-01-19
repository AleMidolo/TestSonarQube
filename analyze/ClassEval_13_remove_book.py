def remove_book(self, title, quantity):
    """
    इन्वेंटरी से एक या कई किताबें हटाएं जो किताब के शीर्षक द्वारा क्रमबद्ध है।
    अमान्य इनपुट मिलने पर झूठा उठाएं।
    :param title: str, किताब का शीर्षक
    :param quantity: int
    """
    # Validate input types
    if not isinstance(title, str):
        raise ValueError("Title must be a string")
    
    if not isinstance(quantity, int):
        raise ValueError("Quantity must be an integer")
    
    # Validate quantity is positive
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    
    # Check if title exists in inventory
    if not hasattr(self, 'inventory'):
        self.inventory = {}
    
    if title not in self.inventory:
        raise ValueError(f"Book with title '{title}' not found in inventory")
    
    # Check if sufficient quantity exists
    if self.inventory[title] < quantity:
        raise ValueError(f"Insufficient quantity. Only {self.inventory[title]} copies available")
    
    # Remove the books
    self.inventory[title] -= quantity
    
    # Remove entry if quantity becomes 0
    if self.inventory[title] == 0:
        del self.inventory[title]