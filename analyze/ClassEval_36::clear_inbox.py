def clear_inbox(self, size):
        """
        ईमेल बॉक्स को साफ करता है, सबसे पुराने ईमेल को हटाकर जब तक ईमेल बॉक्स में दिए गए आकार के लिए पर्याप्त स्थान नहीं हो जाता।
        :param size: ईमेल का आकार, फ्लोट।
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.inbox = [{'size': 10},{'size': 20},{'size': 15}]
        >>> receiver.clear_inbox(30)
        >>> receiver.inbox
        [{'size': 15}]
        """
        while self.get_occupied_size() + size > self.capacity and self.inbox:
            self.inbox.pop(0)