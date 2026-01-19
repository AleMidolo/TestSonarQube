def match(self, pattern, text):
    """
        जांचें कि क्या पाठ नियमित अभिव्यक्ति से मेल खाता है
        :param pattern: स्ट्रिंग, नियमित अभिव्यक्ति पैटर्न
        :param text: स्ट्रिंग, मेल खाने के लिए पाठ
        :return: True या False, यह दर्शाते हुए कि पाठ नियमित अभिव्यक्ति से मेल खाता है या नहीं
        >>> ru = RegexUtils()
        >>> ru.match(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890")
        True
        """
    return re.match(pattern, text) is not None