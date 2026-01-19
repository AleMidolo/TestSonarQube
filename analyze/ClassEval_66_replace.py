def replace(self, string):
    """
        Reemplaza las referencias de caracteres numéricos (entidades HTML) en la cadena de entrada por sus correspondientes caracteres Unicode.
        :param string: str, la cadena de entrada que contiene referencias de caracteres numéricos.
        :return: str, la cadena de entrada con las referencias de caracteres numéricos reemplazadas por sus correspondientes caracteres Unicode.
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
        if string[i:i + 2] == '&#':
            j = i + 2
            is_hex = False
            if j < length and string[j] == 'x':
                is_hex = True
                j += 1
            start_num = j
            while j < length and string[j] != ';':
                j += 1
            if j < length and string[j] == ';':
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