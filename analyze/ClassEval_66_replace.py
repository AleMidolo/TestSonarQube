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
                            if all((self.is_hex_char(c) for c in num_str)):
                                code_point = int(num_str, 16)
                            else:
                                result.append(string[i:j + 1])
                                i = j + 1
                                continue
                        elif num_str.isdigit():
                            code_point = int(num_str)
                        else:
                            result.append(string[i:j + 1])
                            i = j + 1
                            continue
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