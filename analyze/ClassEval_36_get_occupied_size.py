def get_occupied_size(self):
    """
        Retrieves the total size of emails in the email box.
        :return: The total size of emails in the email box, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        >>> sender.get_occupied_size()
        10
        """
    return sum((email['size'] for email in self.inbox))