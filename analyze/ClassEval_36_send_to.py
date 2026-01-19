def send_to(self, recv, content, size):
    """
    发送电子邮件到给定的电子邮件地址。
    :param recv: 接收者的电子邮件地址，str。
    :param content: 电子邮件的内容，str。
    :param size: 电子邮件的大小，float。
    :return: 如果电子邮件成功发送则返回 True，如果接收者的邮箱已满则返回 False。
    """
    from datetime import datetime
    
    # Check if receiver has enough space
    if recv.get_occupied_size() + size > recv.capacity:
        return False
    
    # Create email message
    email = {
        'sender': self.address,
        'receiver': recv.address,
        'content': content,
        'size': size,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'unread'
    }
    
    # Add to receiver's inbox
    recv.inbox = email
    
    return True