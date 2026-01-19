def clear_inbox(self, size):
    """
    通过删除最旧的电子邮件来清空邮箱,直到邮箱有足够的空间来容纳给定的大小。
    :param size: 电子邮件的大小,浮点数。
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
    >>> receiver.clear_inbox(30)
    >>> receiver.inbox
    [{'size': 15}]

    """
    # Calculate current inbox size
    current_size = sum(email['size'] for email in self.inbox)
    
    # Calculate available space
    available_space = self.capacity - current_size
    
    # If there's already enough space, no need to delete anything
    if available_space >= size:
        return
    
    # Calculate how much space we need to free
    space_needed = size - available_space
    
    # Delete oldest emails (from the beginning of the list) until we have enough space
    freed_space = 0
    while freed_space < space_needed and self.inbox:
        freed_space += self.inbox[0]['size']
        self.inbox.pop(0)