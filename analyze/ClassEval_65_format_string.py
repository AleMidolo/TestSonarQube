def format_string(self, x):
    """
        Convierte una representación de cadena de un número en formato de palabras
        :param x: str, la representación de cadena de un número
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "UNO CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
        """
    if not x:
        return ''
    is_negative = False
    if x[0] == '-':
        is_negative = True
        x = x[1:]
    parts = x.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_words = self._format_integer_part(integer_part)
    decimal_words = ''
    if decimal_part:
        decimal_words = self._format_decimal_part(decimal_part)
    result = ''
    if is_negative:
        result += 'MINUS '
    result += integer_words
    if decimal_words:
        result += ' AND ' + decimal_words
    result += ' ONLY'
    return result.strip()