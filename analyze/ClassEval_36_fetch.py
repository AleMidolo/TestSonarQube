def fetch(self):
    """
        Recupera el primer correo electrónico no leído en la bandeja de entrada y lo marca como leído.
        :return: El primer correo electrónico no leído en la bandeja de entrada, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hola', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hola', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

        """
    for email in self.inbox:
        if email['state'] == 'unread':
            email['state'] = 'read'
            return email
    return None