def get_occupied_size(self):
    """
        Obtains the total size of the emails in the inbox.
        :return: The total size of the emails in the inbox, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hola', 'size': 10, 'time': datetime.now, 'state': 'no leído'}]
        >>> sender.get_occupied_size()
        10
        """
    return sum((email['size'] for email in self.inbox))