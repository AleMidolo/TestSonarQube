def format(self, x):
    """
        Convierte un número en formato de palabras
        :param x: int o float, el número que se va a convertir en formato de palabras
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
        """
    if isinstance(x, float):
        x = f'{x:.2f}'
    elif isinstance(x, int):
        x = str(x)
    else:
        raise ValueError('Input must be an integer or float.')
    return self.format_string(x).replace('ONLY', 'SOLAMENTE').replace('AND', 'Y')