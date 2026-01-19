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
    length = len(string)
    while i < length:
        if string[i] == '&' and i + 1 < length and (string[i + 1] == '#'):
            j = i + 2
            is_hex = False
            if j < length and (string[j] == 'x' or string[j] == 'X'):
                is_hex = True
                j += 1
            start_num = j
            while j < length and (string[j].isdigit() or (is_hex and self.is_hex_char(string[j]))):
                j += 1
            if j < length and string[j] == ';' and (j > start_num):
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