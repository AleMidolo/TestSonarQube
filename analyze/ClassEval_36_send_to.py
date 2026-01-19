def send_to(self, recv, content, size):
    """
        दिए गए ईमेल पते पर एक ईमेल भेजता है।
        :param recv: रिसीवर का ईमेल पता, str.
        :param content: ईमेल की सामग्री, str.
        :param size: ईमेल का आकार, float.
        :return: यदि ईमेल सफलतापूर्वक भेजा गया है तो True, यदि रिसीवर का ईमेल बॉक्स भरा हुआ है तो False.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.send_to(receiver, 'Hello', 10)
        True
        >>> receiver.inbox
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}

        """
    if recv.is_full_with_one_more_email(size):
        return False
    if recv.get_occupied_size() + size > recv.capacity:
        recv.clear_inbox(size)
    email = {'sender': self.addr, 'receiver': recv.addr, 'content': content, 'size': size, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'state': 'unread'}
    recv.inbox.append(email)
    return True