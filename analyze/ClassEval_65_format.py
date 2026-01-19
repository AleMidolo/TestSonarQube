def format(self, x):
    """
        Convierte un número en formato de palabras
        :param x: int o float, el número que se va a convertir en formato de palabras
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
        """
    if isinstance(x, (int, float)):
        x_str = str(x)
        if isinstance(x, float):
            if 'e' in x_str.lower():
                x_str = format(x, 'f')
            if '.' in x_str:
                integer_part, decimal_part = x_str.split('.')
                decimal_part = decimal_part.rstrip('0')
                if decimal_part:
                    x_str = f'{integer_part}.{decimal_part}'
                else:
                    x_str = integer_part
    else:
        x_str = str(x)
    return self.format_string(x_str)