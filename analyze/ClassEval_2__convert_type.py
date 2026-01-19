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
    if arg in self.types:
        if self.types[arg] == int:
            return int(value)
        elif self.types[arg] == float:
            return float(value)
        elif self.types[arg] == bool:
            return value.lower() in ('true', '1', 'yes')
    return value