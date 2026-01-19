def get_occupied_size(self):
    """
    Obtiene el tamaño total de los correos electrónicos en la bandeja de entrada.
    :return: El tamaño total de los correos electrónicos en la bandeja de entrada, float.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hola', 'size': 10, 'time': datetime.now, 'state': 'no leído'}]
    >>> sender.get_occupied_size()
    10

    """
    total_size = 0
    for email in self.inbox:
        total_size += email['size']
    return total_size