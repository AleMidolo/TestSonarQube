def is_full_with_one_more_email(self, size):
    """
    Determina se la casella di posta è piena dopo aver aggiunto un'email della dimensione data.
    :param size: La dimensione dell'email, float.
    :return: True se la casella di posta è piena, False altrimenti.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.is_full_with_one_more_email(10)
    False

    """
    return self.current_size + size > self.capacity