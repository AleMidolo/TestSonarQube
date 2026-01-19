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
            if x.is_integer():
                x_str = str(int(x))
            else:
                x_str = format(x, 'f').rstrip('0').rstrip('.')
    else:
        x_str = str(x)
    return self.format_string(x_str)