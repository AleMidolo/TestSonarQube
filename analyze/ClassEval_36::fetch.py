def fetch(self):
    """
        检索邮箱中第一封未读邮件并将其标记为已读。
        :return: 邮箱中第一封未读邮件，dict。
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