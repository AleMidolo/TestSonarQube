def format(self, x):
    """
        Converte un numero nella sua rappresentazione in parole.
        :param x: int o float, il numero da convertire in formato parole
        :return: str, il numero in formato parole
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CENTO VENTITRE MILA QUATTROCENTO CINQUANTA SEI SOLO"
        """
    if isinstance(x, int):
        return self.format_string(str(x))
    elif isinstance(x, float):
        return self.format_string(f'{x:.2f}')
    else:
        raise ValueError('Input must be an integer or float.')