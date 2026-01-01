def get_occupied_size(self):
    """
        Ottiene la dimensione totale delle email nella casella di posta.
        :return: La dimensione totale delle email nella casella di posta, float.
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Ciao', 'size': 10, 'time': datetime.now, 'state': 'non letto'}]
        >>> sender.get_occupied_size()
        10
        """
    return sum((email['size'] for email in self.inbox))