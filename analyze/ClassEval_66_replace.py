def replace(self, string):
    """
        Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
        :param string: str, the input string containing numeric character references.
        :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
        >>> unescaper = NumericEntityUnescaper()
        >>> unescaper.replace("&#65;&#66;&#67;")
        'ABC'

        """
    if not string:
        return string
    result = []
    i = 0
    n = len(string)
    while i < n:
        if string[i] == '&' and i + 1 < n and (string[i + 1] == '#'):
            j = i + 2
            is_hex = False
            if j < n and (string[j] == 'x' or string[j] == 'X'):
                is_hex = True
                j += 1
            start_num = j
            while j < n and (string[j].isdigit() or (is_hex and self.is_hex_char(string[j]))):
                j += 1
            if j < n and string[j] == ';' and (j > start_num):
                num_str = string[start_num:j]
                try:
                    if is_hex:
                        code_point = int(num_str, 16)
                    else:
                        code_point = int(num_str)
                    if 0 <= code_point <= 1114111:
                        result.append(chr(code_point))
                        i = j + 1
                        continue
                except (ValueError, OverflowError):
                    pass
        result.append(string[i])
        i += 1
    return ''.join(result)