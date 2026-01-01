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
    self.arguments.clear()
    parts = command_string.split()
    i = 0
    while i < len(parts):
        part = parts[i]
        if part.startswith('--'):
            if '=' in part:
                arg_name, arg_value = part[2:].split('=', 1)
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
            else:
                arg_name = part[2:]
                self.arguments[arg_name] = True
        elif part.startswith('-') and (not part.startswith('--')):
            arg_name = part[1:]
            if i + 1 < len(parts) and (not parts[i + 1].startswith('-')):
                arg_value = parts[i + 1]
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
                i += 1
            else:
                self.arguments[arg_name] = True
        i += 1
    missing_args = set()
    for req_arg in self.required:
        if req_arg not in self.arguments:
            missing_args.add(req_arg)
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)