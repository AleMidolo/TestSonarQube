def sub(self, pattern, replacement, text):
        """
        नियमित अभिव्यक्ति द्वारा मेल खाती उपस्ट्रिंग को निर्दिष्ट स्ट्रिंग से बदलें
        :param pattern: स्ट्रिंग, नियमित अभिव्यक्ति पैटर्न
        :param replacement: बदलने के लिए पाठ
        :param text: स्ट्रिंग, जिसे बदला जाना है
        :return: स्ट्रिंग, प्रतिस्थापन के बाद का पाठ
        >>> ru = RegexUtils()
        >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        'phone num abiguygusu phone num kjgufwycs phone num'
        """
        return re.sub(pattern, replacement, text)