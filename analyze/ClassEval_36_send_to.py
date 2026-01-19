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
    if recv.is_full_with_one_more_email(size):
        return False
    recv.clear_inbox(size)
    email = {'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': size, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'state': 'unread'}
    recv.inbox.append(email)
    return True