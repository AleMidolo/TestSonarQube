def format(self, x):
    """
        Converte un numero nella sua rappresentazione in parole.
        :param x: int o float, il numero da convertire in formato parole
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CENTO VENTITRE MILA QUATTROCENTO CINQUANTA SEI SOLO"
        """
    if isinstance(x, (int, float)):
        x_str = str(x)
        if isinstance(x, float):
            x_str = str(x).rstrip('0').rstrip('.') if '.' in str(x) else str(x)
        return self.format_string(x_str)
    else:
        raise TypeError('Input must be int or float')