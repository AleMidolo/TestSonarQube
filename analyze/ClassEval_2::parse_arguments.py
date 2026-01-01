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
    import re
    pattern = '--(\\w+)=([\\w\\d]+)|-(\\w+)|--(\\w+)'
    matches = re.findall(pattern, command_string)
    for match in matches:
        if match[0]:
            arg_name = match[0]
            value = match[1]
            self.arguments[arg_name] = self._convert_type(arg_name, value)
        elif match[2]:
            arg_name = match[2]
            self.arguments[arg_name] = True
        elif match[3]:
            arg_name = match[3]
            self.arguments[arg_name] = True
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)