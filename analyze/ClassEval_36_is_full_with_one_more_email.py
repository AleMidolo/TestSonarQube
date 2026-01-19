def is_full_with_one_more_email(self, size):
    """
        यह निर्धारित करता है कि क्या ईमेल बॉक्स एक दिए गए आकार के ईमेल को जोड़ने के बाद भरा हुआ है।
        :param size: ईमेल का आकार, फ्लोट।
        :return: यदि ईमेल बॉक्स भरा हुआ है तो True, अन्यथा False।
        >>> sender = EmailClient('sender@example.com', 100)
        >>> receiver = EmailClient('receiver@example.com', 50)
        >>> receiver.is_full_with_one_more_email(10)
        False

        """
    current_occupied = self.get_occupied_size()
    return current_occupied + size > self.capacity