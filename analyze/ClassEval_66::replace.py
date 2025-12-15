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
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'
        """
        import re

        def replace_entity(match):
            num = match.group(1)
            if num.startswith('x'):
                return chr(int(num[1:], 16))
            else:
                return chr(int(num))

        return re.sub(r'&#(x?[0-9a-fA-F]+);', replace_entity, string)