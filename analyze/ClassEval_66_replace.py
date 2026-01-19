import re

def replace(self, string):
    """
    将输入字符串中的数字字符引用（HTML 实体）替换为相应的 Unicode 字符。
    :param string: str，包含数字字符引用的输入字符串。
    :return: str，输入字符串，其中的数字字符引用已被相应的 Unicode 字符替换。
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    def replace_entity(match):
        entity = match.group(0)
        # 处理十六进制格式 &#xHHHH; 或 &#XHHHH;
        if entity[2] in ('x', 'X'):
            code_point = int(entity[3:-1], 16)
        # 处理十进制格式 &#DDDD;
        else:
            code_point = int(entity[2:-1], 10)
        
        # 将数字转换为对应的 Unicode 字符
        try:
            return chr(code_point)
        except (ValueError, OverflowError):
            # 如果代码点无效，返回原始实体
            return entity
    
    # 匹配十进制和十六进制的数字字符引用
    # &#数字; 或 &#x十六进制数字; 或 &#X十六进制数字;
    pattern = r'&#[xX]?[0-9a-fA-F]+;'
    
    return re.sub(pattern, replace_entity, string)