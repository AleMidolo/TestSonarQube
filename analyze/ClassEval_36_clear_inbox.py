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
    current_size = sum(email['size'] for email in self.inbox)
    available_space = self.capacity - current_size
    
    while available_space < size and self.inbox:
        oldest_email = self.inbox.pop(0)
        available_space += oldest_email['size']