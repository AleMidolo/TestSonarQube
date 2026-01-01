def _convert_type(self, arg, value):
    """
        尝试通过在 self.types 中查找来转换输入值的类型。
        :param value: 字符串, 命令行中的输入值
        :return: 如果成功转换，则返回 self.types 中对应的值，否则返回输入值
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
    if arg in self.types:
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value
    return value