def send_to(self, recv, content, size):
    """
        发送电子邮件到给定的电子邮件地址。
        :param recv: 接收者的电子邮件地址，str。
        :param content: 电子邮件的内容，str。
        :param size: 电子邮件的大小，float。
        :return: 如果电子邮件成功发送则返回 True，如果接收者的邮箱已满则返回 False。
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}
        """
    if recv.is_full_with_one_more_email(size):
        return False
    email = {'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': size, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'state': 'unread'}
    recv.inbox.append(email)
    return True