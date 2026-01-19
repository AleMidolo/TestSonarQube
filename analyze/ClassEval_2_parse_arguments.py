def parse_arguments(self, command_string):
    """
        Analiza la cadena de argumentos de línea de comandos dada e invoca _convert_type para almacenar el resultado analizado en un tipo específico en el diccionario de argumentos.
        Verifica si faltan argumentos requeridos, si los hay, y devuelve False con los nombres de los argumentos faltantes; de lo contrario, devuelve True.
        :param command_string: str, cadena de argumentos de línea de comandos, formateada como "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) si el análisis es exitoso, (False, missing_args) si el análisis falla,
            donde missing_args es un conjunto de los nombres de los argumentos faltantes que son str.
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
    args = command_string.split()[1:]
    missing_args = set()
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
        else:
            key = arg
            value = True
        if key.startswith('--'):
            key = key[2:]
        elif key.startswith('-'):
            key = key[1:]
        if key in self.types:
            self.arguments[key] = self._convert_type(key, value)
        else:
            self.arguments[key] = value
    for req_arg in self.required:
        if req_arg not in self.arguments:
            missing_args.add(req_arg)
    return (len(missing_args) == 0, missing_args if missing_args else None)