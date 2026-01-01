def clear_inbox(self, size):
    """
        Pulisce la casella di posta eliminando le email più vecchie fino a quando la casella di posta ha spazio sufficiente per accogliere la dimensione data.
        :param size: La dimensione dell'email, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]

        """
    for email in self.inbox:
        if 'time' in email and isinstance(email['time'], str):
            email['time_dt'] = datetime.strptime(email['time'], '%Y-%m-%d %H:%M:%S')
        else:
            email['time_dt'] = datetime.min
    self.inbox.sort(key=lambda x: x['time_dt'])
    for email in self.inbox:
        if 'time_dt' in email:
            del email['time_dt']
    while self.is_full_with_one_more_email(size) and len(self.inbox) > 0:
        self.inbox.pop(0)