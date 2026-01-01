def get_argument(self, key):
    """
        Recupera el valor del argumento especificado del diccionario de argumentos y lo devuelve.
        :param key: str, nombre del argumento
        :return: El valor del argumento, o None si el argumento no existe.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
    return self.arguments.get(key, None)