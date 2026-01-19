def replace(self, string):
    """
    将输入字符串中的数字字符引用（HTML 实体）替换为相应的 Unicode 字符。
    :param string: str，包含数字字符引用的输入字符串。
    :return: str，输入字符串，其中的数字字符引用已被相应的 Unicode 字符替换。
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    import re
    
    def replace_entity(match):
        entity = match.group(0)
        # 提取数字部分
        if entity.startswith('&#x') or entity.startswith('&#X'):
            # 十六进制格式 &#xHHH; 或 &#XHHH;
            num_str = entity[3:-1]
            code_point = int(num_str, 16)
        else:
            # 十进制格式 &#DDD;
            num_str = entity[2:-1]
            code_point = int(num_str, 10)
        
        return chr(code_point)
    
    # 匹配十进制和十六进制的数字字符引用
    # &#数字; 或 &#x十六进制数字; 或 &#X十六进制数字;
    pattern = r'&#[xX][0-9a-fA-F]+;|&#\d+;'
    result = re.sub(pattern, replace_entity, string)
    
    return result