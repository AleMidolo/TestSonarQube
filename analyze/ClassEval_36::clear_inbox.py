def clear_inbox(self, size):
    """
        通过删除最旧的电子邮件来清空邮箱，直到邮箱有足够的空间来容纳给定的大小。
        :param size: 电子邮件的大小，浮点数。
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