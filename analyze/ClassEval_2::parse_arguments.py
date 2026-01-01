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
    self.arguments = {}
    tokens = command_string.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.startswith('--') and '=' in token:
            arg_name = token[2:].split('=')[0]
            arg_value = token.split('=', 1)[1]
            converted_value = self._convert_type(arg_name, arg_value)
            self.arguments[arg_name] = converted_value
            i += 1
        elif token.startswith('--'):
            arg_name = token[2:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                arg_value = tokens[i + 1]
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
                i += 2
            else:
                self.arguments[arg_name] = True
                i += 1
        elif token.startswith('-') and len(token) > 1 and (not token.startswith('--')):
            arg_name = token[1:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                arg_value = tokens[i + 1]
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
                i += 2
            else:
                self.arguments[arg_name] = True
                i += 1
        else:
            i += 1
    missing_args = set()
    for req_arg in self.required:
        if req_arg not in self.arguments:
            missing_args.add(req_arg)
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)