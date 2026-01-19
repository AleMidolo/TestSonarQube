def replace(self, string):
    """
        Sostituisce i riferimenti ai caratteri numerici (entità HTML) nella stringa di input con i loro corrispondenti caratteri Unicode.
        :param string: str, la stringa di input contenente riferimenti ai caratteri numerici.
        :return: str, la stringa di input con i riferimenti ai caratteri numerici sostituiti con i loro corrispondenti caratteri Unicode.
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
        if string[i:i + 2] == '&#':
            j = i + 2
            is_hex = False
            if j < n and string[j] == 'x':
                is_hex = True
                j += 1
            start_num = j
            while j < n and string[j] != ';':
                j += 1
            if j < n and string[j] == ';':
                num_str = string[start_num:j]
                if num_str:
                    try:
                        if is_hex:
                            code_point = int(num_str, 16)
                        else:
                            code_point = int(num_str)
                        if 0 <= code_point <= 1114111:
                            result.append(chr(code_point))
                        else:
                            result.append(string[i:j + 1])
                    except (ValueError, OverflowError):
                        result.append(string[i:j + 1])
                    i = j + 1
                    continue
        result.append(string[i])
        i += 1
    return ''.join(result)