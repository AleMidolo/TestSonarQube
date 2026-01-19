def send_to(self, recv, content, size):
    """
    Sends an email to the given email address.
    :param recv: The email address of the receiver, str.
    :param content: The content of the email, str.
    :param size: The size of the email, float.
    :return: True if the email is sent successfully, False if the receiver's email box is full.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> sender.send_to(receiver, 'Hello', 10)
    True
    >>> receiver.inbox
    {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

    """
    from datetime import datetime
    
    # Check if receiver has enough space in their inbox
    current_size = sum(email.get('size', 0) for email in recv.inbox) if isinstance(recv.inbox, list) else recv.inbox.get('size', 0) if isinstance(recv.inbox, dict) else 0
    
    # If recv.inbox is a list, calculate total size
    if isinstance(recv.inbox, list):
        current_size = sum(email.get('size', 0) for email in recv.inbox)
    elif isinstance(recv.inbox, dict):
        current_size = recv.inbox.get('size', 0)
    else:
        current_size = 0
    
    # Check if adding this email would exceed capacity
    if current_size + size > recv.capacity:
        return False
    
    # Create email object
    email = {
        'sender': self.email,
        'receiver': recv.email,
        'content': content,
        'size': size,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'unread'
    }
    
    # Add email to receiver's inbox
    recv.inbox = email
    
    return True