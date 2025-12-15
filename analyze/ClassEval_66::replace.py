class NumericEntityUnescaper: 
    def __init__(self):
        pass

    @staticmethod
    def is_hex_char(char):
        """
            Determines whether a given character is a hexadecimal digit.
            :param char: str, the character to check.
            :return: bool, True if the character is a hexadecimal digit, False otherwise.
            >>> NumericEntityUnescaper.is_hex_char('a')
            True
        """
        return char.isdigit() or ('a' <= char.lower() <= 'f')

    def replace(self, string):
        """
        इनपुट स्ट्रिंग में संख्या वर्ण संदर्भ (HTML संस्थाएँ) को उनके संबंधित यूनिकोड वर्णों के साथ बदलता है।
        :param string: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ शामिल हैं।
        :return: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ को उनके संबंधित यूनिकोड वर्णों के साथ बदला गया है।
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'
        """
        import re

        def replace_entity(match):
            num = int(match.group(1))
            return chr(num)

        return re.sub(r'&#(\d+);', replace_entity, string)