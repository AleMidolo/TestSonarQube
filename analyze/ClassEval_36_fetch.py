def fetch(self):
    """
    Recupera la prima email non letta nella casella di posta e la segna come letta.
    :return: La prima email non letta nella casella di posta, dict.
    >>> sender = EmailClient('sender@example.com', 100)
    >>> receiver = EmailClient('receiver@example.com', 50)
    >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Ciao', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
    >>> receiver.fetch()
    {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Ciao', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

    """
    for email in self.inbox:
        if email['state'] == 'unread':
            email['state'] = 'read'
            return email
    return None