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
        code = int(match.group(1))
        return chr(code)
    return re.sub('&#(\\d+);', replace_entity, string)