def replace(self, string):
    """
        इनपुट स्ट्रिंग में संख्या वर्ण संदर्भ (HTML संस्थाएँ) को उनके संबंधित यूनिकोड वर्णों के साथ बदलता है।
        :param string: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ शामिल हैं।
        :return: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ को उनके संबंधित यूनिकोड वर्णों के साथ बदला गया है।
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
    result = []
    i = 0
    length = len(string)
    while i < length:
        if string[i:i + 2] == '&#':
            j = i + 2
            is_hex = False
            if j < length and string[j] == 'x':
                is_hex = True
                j += 1
            start = j
            while j < length and self.is_hex_char(string[j]):
                j += 1
            if j < length and string[j] == ';':
                num_str = string[start:j]
                if num_str:
                    try:
                        if is_hex:
                            code_point = int(num_str, 16)
                        else:
                            code_point = int(num_str)
                        if 0 <= code_point <= 1114111:
                            result.append(chr(code_point))
                            i = j + 1
                            continue
                    except ValueError:
                        pass
        result.append(string[i])
        i += 1
    return ''.join(result)