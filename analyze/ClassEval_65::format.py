def format(self, x):
    """
        Converts a number into words format
        :param x: int or float, the number to be converted into words format
        :return: str, the number in words format
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "ONE HUNDRED AND TWENTY THREE THOUSAND FOUR HUNDRED AND FIFTY SIX ONLY"
        """
    if isinstance(x, int):
        return self.format_string(str(x))
    elif isinstance(x, float):
        return self.format_string(str(x))
    else:
        raise TypeError('Input must be int or float')