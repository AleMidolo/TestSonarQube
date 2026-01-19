def get_occupied_size(self):
    """
        获取邮箱中邮件的总大小。
        :return: 邮箱中邮件的总大小，浮点数。
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        >>> sender.get_occupied_size()
        10
        """
    return sum((email['size'] for email in self.inbox))