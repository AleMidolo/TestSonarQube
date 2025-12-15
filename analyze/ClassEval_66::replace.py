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
        Sostituisce i riferimenti ai caratteri numerici (entità HTML) nella stringa di input con i loro corrispondenti caratteri Unicode.
        :param string: str, la stringa di input contenente riferimenti ai caratteri numerici.
        :return: str, la stringa di input con i riferimenti ai caratteri numerici sostituiti con i loro corrispondenti caratteri Unicode.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'
        """
        import re

        def replace_entity(match):
            code = int(match.group(1))
            return chr(code)

        return re.sub(r'&#(\d+);', replace_entity, string)