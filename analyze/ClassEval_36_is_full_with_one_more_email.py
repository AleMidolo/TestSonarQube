def is_full_with_one_more_email(self, size):
    """
    确定在添加一个给定大小的电子邮件后，邮箱是否已满。
    :param size: 电子邮件的大小，浮点数。
    :return: 如果邮箱已满则返回 True，否则返回 False。
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.is_full_with_one_more_email(10)
    False

    """
    return self.current_size + size >= self.capacity