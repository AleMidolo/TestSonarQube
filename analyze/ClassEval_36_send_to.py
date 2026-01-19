def send_to(self, recv, content, size):
    """
    Invia un'email all'indirizzo email fornito.
    :param recv: L'indirizzo email del destinatario, str.
    :param content: Il contenuto dell'email, str.
    :param size: La dimensione dell'email, float.
    :return: True se l'email è stata inviata con successo, False se la casella di posta del destinatario è piena.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> sender.send_to(receiver, 'Hello', 10)
    True
    >>> receiver.inbox
    {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

    """
    from datetime import datetime
    
    # Check if receiver's inbox has enough space
    if hasattr(recv, 'capacity') and hasattr(recv, 'inbox'):
        # Calculate current inbox size
        current_size = 0
        if isinstance(recv.inbox, list):
            current_size = sum(email.get('size', 0) for email in recv.inbox)
        elif isinstance(recv.inbox, dict) and 'size' in recv.inbox:
            current_size = recv.inbox.get('size', 0)
        
        # Check if there's enough capacity
        if current_size + size > recv.capacity:
            return False
    
    # Create email object
    email = {
        'sender': self.email if hasattr(self, 'email') else str(self),
        'receiver': recv.email if hasattr(recv, 'email') else str(recv),
        'content': content,
        'size': size,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'unread'
    }
    
    # Add email to receiver's inbox
    if isinstance(recv.inbox, list):
        recv.inbox.append(email)
    else:
        recv.inbox = email
    
    return True