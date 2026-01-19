def generate_split_sentences_pattern(self):
    """
        दो वाक्यों के मध्य के अक्षरों से मेल खाने वाले नियमित अभिव्यक्ति पैटर्न उत्पन्न करें
        :return: स्ट्रिंग, नियमित अभिव्यक्ति पैटर्न जो दो वाक्यों के मध्य के अक्षरों से मेल खाते हैं
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\\s]{1,2}(?=[A-Z])'
        """
    pattern = '[.!?][\\s]{1,2}(?=[A-Z])'
    return pattern