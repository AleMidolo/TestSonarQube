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
    if current_size + size <= self.capacity:
        return
    for email in self.inbox:
        if 'time' in email:
            email['time_dt'] = datetime.strptime(email['time'], '%Y-%m-%d %H:%M:%S')
        else:
            email['time_dt'] = datetime.min
    self.inbox.sort(key=lambda x: x['time_dt'])
    while self.inbox and self.get_occupied_size() + size > self.capacity:
        self.inbox.pop(0)
    for email in self.inbox:
        if 'time_dt' in email:
            del email['time_dt']