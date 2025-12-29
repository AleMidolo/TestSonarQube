def send_to(self, recv, content, size):
    """
        Sends an email to the given email address.
        :param recv: The email address of the receiver, str.
        :param content: The content of the email, str.
        :param size: The size of the email, float.
        :return: True if the email is sent successfully, False if the receiver's email box is full.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]

        """
    if recv.is_full_with_one_more_email(size):
        return False
    occupied = recv.get_occupied_size()
    if occupied + size > recv.capacity:
        space_needed = occupied + size - recv.capacity
        recv.clear_inbox(space_needed)
    email = {'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': size, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'state': 'unread'}
    recv.inbox.append(email)
    return True