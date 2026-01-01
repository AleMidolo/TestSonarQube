def _convert_type(self, arg, value):
    """
        Intenta convertir el tipo del valor de entrada buscando en self.types.
        :param value: str, el valor de entrada en la línea de comandos
        :return: devuelve el valor correspondiente en self.types si se convierte con éxito, o el valor de entrada en caso contrario
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
    arg_type = self.types.get(arg, str)
    try:
        return arg_type(value)
    except ValueError:
        return value