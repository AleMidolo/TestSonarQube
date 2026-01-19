def _convert_type(self, arg, value):
    """
    Try to convert the type of input value by searching in self.types.
    :param value: str, the input value in command line
    :return: return corresponding value in self.types if convert successfully, or the input value oherwise
    >>> parser.types
    {'arg1': int}
    >>> parser._convert_type('arg1', '21')
    21
    """
    if hasattr(self, 'types') and arg in self.types:
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value
    return value