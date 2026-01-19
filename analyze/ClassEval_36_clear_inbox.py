def clear_inbox(self, size):
    """
    Clears the email box by deleting the oldest emails until the email box has enough space to accommodate the given size.
    :param size: The size of the email, float.
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
    
    # Delete oldest emails (from the beginning) until we have enough space
    freed_space = 0
    while freed_space < space_needed and self.inbox:
        freed_space += self.inbox[0]['size']
        self.inbox.pop(0)