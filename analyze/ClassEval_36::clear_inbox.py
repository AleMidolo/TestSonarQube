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
    current_size = self.get_occupied_size()
    if current_size + size <= self.capacity:
        return
    while self.inbox and current_size + size > self.capacity:
        removed_email = self.inbox.pop(0)
        current_size -= removed_email['size']