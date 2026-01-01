def replace(self, string):
    """
        将输入字符串中的数字字符引用（HTML 实体）替换为相应的 Unicode 字符。
        :param string: str，包含数字字符引用的输入字符串。
        :return: str，输入字符串，其中的数字字符引用已被相应的 Unicode 字符替换。
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
            while j < n and string[j] != ';':
                if not (string[j].isdigit() or (is_hex and self.is_hex_char(string[j]))):
                    break
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
        else:
            result.append(string[i])
            i += 1
    return ''.join(result)