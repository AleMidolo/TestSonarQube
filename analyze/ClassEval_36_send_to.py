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
    if hasattr(recv, 'capacity') and hasattr(recv, 'inbox'):
        # Calculate current inbox size
        current_size = 0
        if isinstance(recv.inbox, list):
            for email in recv.inbox:
                current_size += email.get('size', 0)
        elif isinstance(recv.inbox, dict):
            current_size = recv.inbox.get('size', 0)
        
        # Check if there's enough capacity
        if current_size + size > recv.capacity:
            return False
        
        # Create email object
        email = {
            'sender': self.email,
            'receiver': recv.email if hasattr(recv, 'email') else recv,
            'content': content,
            'size': size,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'state': 'unread'
        }
        
        # Add to receiver's inbox
        if isinstance(recv.inbox, list):
            recv.inbox.append(email)
        else:
            recv.inbox = email
        
        return True
    else:
        # If recv is just a string (email address)
        return True