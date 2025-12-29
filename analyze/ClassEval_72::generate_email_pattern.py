def generate_email_pattern(self):
    """
        ईमेल पते से मेल खाने वाले नियमित अभिव्यक्ति पैटर्न उत्पन्न करें
        :return: स्ट्रिंग, नियमित अभिव्यक्ति पैटर्न जो ईमेल पते से मेल खाते हैं
        >>> ru = RegexUtils()
        >>> ru.generate_email_pattern()
        '\x08[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\x08'
        """
    pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'
    return pattern