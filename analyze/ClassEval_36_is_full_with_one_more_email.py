def is_full_with_one_more_email(self, size):
    """
        Determines if the inbox is full after adding an email of the given size.
        :param size: The size of the email, float.
        :return: True if the inbox is full, False otherwise.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False
        """
    return self.get_occupied_size() + size > self.capacity