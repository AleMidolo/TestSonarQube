def is_full_with_one_more_email(self, size):
    """
        Determina si la bandeja de entrada está llena después de agregar un correo electrónico del tamaño dado.
        :param size: El tamaño del correo electrónico, float.
        :return: True si la bandeja de entrada está llena, False en caso contrario.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False

        """
    return self.get_occupied_size() + size > self.capacity