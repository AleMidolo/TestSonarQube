def format(self, x):
    """
        Convierte un número en formato de palabras
        :param x: int o float, el número que se va a convertir en formato de palabras
        :return: str, el número en formato de palabras
        >>> formatter = NumberWordFormatter()
        >>> formatter.format(123456)
        "CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
        """
    if isinstance(x, int):
        return self.format_string(str(x))
    elif isinstance(x, float):
        return self.format_string(str(x))
    else:
        raise TypeError('El parámetro x debe ser int o float')