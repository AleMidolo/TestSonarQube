def clear_inbox(self, size):
    """
        Pulisce la casella di posta eliminando le email più vecchie fino a quando la casella di posta ha spazio sufficiente per accogliere la dimensione data.
        :param size: La dimensione dell'email, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]

        """
    current_size = self.get_occupied_size()
    while self.inbox and current_size + size > self.capacity:
        removed_email = self.inbox.pop(0)
        current_size -= removed_email['size']