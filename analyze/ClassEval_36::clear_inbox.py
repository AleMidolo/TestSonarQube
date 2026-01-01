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
    current_occupied = self.get_occupied_size()
    if current_occupied + size <= self.capacity:
        return
    space_needed = current_occupied + size - self.capacity
    freed_space = 0
    while self.inbox and freed_space < space_needed:
        freed_space += self.inbox[0]['size']
        self.inbox.pop(0)