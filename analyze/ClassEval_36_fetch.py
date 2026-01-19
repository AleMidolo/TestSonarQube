def fetch(self):
    """
        ईमेल बॉक्स में पहला अप्र прочित ईमेल प्राप्त करता है और इसे पढ़ा हुआ के रूप में चिह्नित करता है।
        :return: ईमेल बॉक्स में पहला अप्र прочित ईमेल, dict.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'unread'}]
        >>> receiver.fetch()
        {'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': '2023-07-13 11:36:40', 'state': 'read'}

        """
    for email in self.inbox:
        if email['state'] == 'unread':
            email['state'] = 'read'
            return email
    return None