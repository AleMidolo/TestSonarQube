def replace(self, string):
    """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
    result = []
    i = 0
    n = len(string)
    while i < n:
        if string[i:i + 2] == '&#':
            j = i + 2
            is_hex = False
            if j < n and string[j] == 'x':
                is_hex = True
                j += 1
            start = j
            while j < n and string[j] != ';':
                j += 1
            if j < n and string[j] == ';':
                entity = string[start:j]
                if entity:
                    try:
                        if is_hex:
                            code_point = int(entity, 16)
                        else:
                            code_point = int(entity)
                        if 0 <= code_point <= 1114111:
                            result.append(chr(code_point))
                        else:
                            result.append(string[i:j + 1])
                    except (ValueError, OverflowError):
                        result.append(string[i:j + 1])
                else:
                    result.append(string[i:j + 1])
                i = j + 1
            else:
                result.append(string[i])
                i += 1
        else:
            result.append(string[i])
            i += 1
    return ''.join(result)