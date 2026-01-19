def _convert_type(self, arg, value):
    """
        Prova a convertire il tipo del valore di input cercando in self.types.
        :param value: str, il valore di input nella riga di comando
        :return: restituisce il valore corrispondente in self.types se la conversione ha successo, altrimenti il valore di input
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