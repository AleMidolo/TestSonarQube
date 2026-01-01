def clear_inbox(self, size):
    """
        Limpia la bandeja de entrada eliminando los correos electrónicos más antiguos hasta que la bandeja de entrada tenga suficiente espacio para acomodar el tamaño dado.
        :param size: El tamaño del correo electrónico, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]

        """
    current_size = self.get_occupied_size()
    while self.inbox and current_size + size > self.capacity:
        removed_email = self.inbox.pop(0)
        current_size -= removed_email['size']