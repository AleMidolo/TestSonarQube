def clear_inbox(self, size):
    """
        Clears the inbox by removing the oldest emails until there is enough space to accommodate the given size.
        :param size: The size of the email, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]
        """
    while self.get_occupied_size() + size > self.capacity and self.inbox:
        self.inbox.pop(0)