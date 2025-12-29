def generate_phone_number_pattern(self):
    """
        फोन नंबरों से मेल खाने वाले नियमित अभिव्यक्ति पैटर्न उत्पन्न करें
        :return: स्ट्रिंग, फोन नंबरों से मेल खाने वाले नियमित अभिव्यक्ति पैटर्न
        >>> ru = RegexUtils()
        >>> ru.generate_phone_number_pattern()
        '\x08\\d{3}-\\d{3}-\\d{4}\x08'
        """
    pattern = '\\b\\d{3}-\\d{3}-\\d{4}\\b'
    return pattern