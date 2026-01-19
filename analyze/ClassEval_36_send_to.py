def send_to(self, recv, content, size):
    """
        Envía un correo electrónico a la dirección de correo electrónico dada.
        :param recv: La dirección de correo electrónico del receptor, str.
        :param content: El contenido del correo electrónico, str.
        :param size: El tamaño del correo electrónico, float.
        :return: True si el correo electrónico se envía con éxito, False si la bandeja de entrada del receptor está llena.
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