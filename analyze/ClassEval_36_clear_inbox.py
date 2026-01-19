def clear_inbox(self, size):
    """
    ईमेल बॉक्स को साफ करता है, सबसे पुराने ईमेल को हटाकर जब तक ईमेल बॉक्स में दिए गए आकार के लिए पर्याप्त स्थान नहीं हो जाता।
    :param size: ईमेल का आकार, फ्लोट।
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    >>> receiver.clear_inbox(30)
    >>> receiver.inbox
    [{'size': 15}]

    """
    # Calculate current inbox size
    current_size = sum(email['size'] for email in self.inbox)
    
    # Calculate available space
    available_space = self.capacity - current_size
    
    # If there's already enough space, no need to clear
    if available_space >= size:
        return
    
    # Calculate how much space we need to free
    space_needed = size - available_space
    
    # Remove oldest emails (from the beginning) until we have enough space
    while self.inbox and space_needed > 0:
        removed_email = self.inbox.pop(0)
        space_needed -= removed_email['size']