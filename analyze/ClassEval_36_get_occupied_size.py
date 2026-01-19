def get_occupied_size(self):
    """
        ईमेल बॉक्स में ईमेल का कुल आकार प्राप्त करता है।
        :return: ईमेल बॉक्स में ईमेल का कुल आकार, फ्लोट।
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> sender.inbox = [{'sender': 'sender@example.com', 'receiver': 'receiver@example.com', 'content': 'Hello', 'size': 10, 'time': datetime.now, 'state': 'unread'}]
        >>> sender.get_occupied_size()
        10

        """
    total_size = 0.0
    for email in self.inbox:
        total_size += email['size']
    return total_size