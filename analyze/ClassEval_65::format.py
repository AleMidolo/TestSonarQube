def format(self, x):
    """
        将数字转换为单词格式
        :param x: int 或 float，要转换为单词格式的数字
        :return: str，数字的单词格式
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if isinstance(x, int):
        return self.format_string(str(x))
    elif isinstance(x, float):
        return self.format_string(str(x))
    else:
        raise TypeError('x must be int or float')