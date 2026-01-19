def fetch(self):
    """
        Retrieves the first unread email in the inbox and marks it as read.
        :return: The first unread email in the inbox, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}
        """
    for email in self.inbox:
        if email['state'] == 'unread':
            email['state'] = 'read'
            return email
    return None