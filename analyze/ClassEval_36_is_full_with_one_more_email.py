def is_full_with_one_more_email(self, size):
    """
    Determines whether the email box is full after adding an email of the given size.
    :param size: The size of the email, float.
    :return: True if the email box is full, False otherwise.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.is_full_with_one_more_email(10)
    False

    """
    return self.current_size + size >= self.capacity