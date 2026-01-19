import re

def split(self, pattern, text):
    """
    नियमित अभिव्यक्ति पैटर्न के आधार पर पाठ को विभाजित करें और उपस्ट्रिंग्स की एक सूची लौटाएं
    :param pattern: स्ट्रिंग, नियमित अभिव्यक्ति पैटर्न
    :param text: स्ट्रिंग, विभाजित करने के लिए पाठ
    :return: स्ट्रिंग की सूची, विभाजन के बाद उपस्ट्रिंग्स की सूची
    >>> ru = RegexUtils()
    >>> ru.split(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['', ' abiguygusu ', ' kjgufwycs ', '']
    """
    return re.split(pattern, text)