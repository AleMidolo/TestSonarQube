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
    if current_size + size <= self.capacity:
        return

    def get_email_time(email):
        if 'time' in email:
            try:
                return datetime.strptime(email['time'], '%Y-%m-%d %H:%M:%S')
            except (ValueError, TypeError):
                return datetime.min
        return datetime.min
    self.inbox.sort(key=get_email_time)
    while self.inbox and self.get_occupied_size() + size > self.capacity:
        self.inbox.pop(0)