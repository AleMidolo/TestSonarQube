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
    # Split the command string into tokens
    tokens = command_string.split()
    
    # Skip the first two tokens (python script.py)
    if len(tokens) >= 2:
        tokens = tokens[2:]
    
    # Initialize arguments dictionary if not exists
    if not hasattr(self, 'arguments'):
        self.arguments = {}
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Check if token starts with -- or -
        if token.startswith('--') or token.startswith('-'):
            # Remove leading dashes
            arg_name = token.lstrip('-')
            
            # Check if it's in format --arg=value
            if '=' in arg_name:
                parts = arg_name.split('=', 1)
                arg_name = parts[0]
                value = parts[1]
                # Convert type if method exists
                if hasattr(self, '_convert_type'):
                    value = self._convert_type(arg_name, value)
                self.arguments[arg_name] = value
                i += 1
            else:
                # Check if next token exists and is not an argument
                if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                    value = tokens[i + 1]
                    # Convert type if method exists
                    if hasattr(self, '_convert_type'):
                        value = self._convert_type(arg_name, value)
                    self.arguments[arg_name] = value
                    i += 2
                else:
                    # It's a flag/option (boolean)
                    self.arguments[arg_name] = True
                    i += 1
        else:
            i += 1
    
    # Check for required arguments
    missing_args = set()
    if hasattr(self, 'required_args'):
        for req_arg in self.required_args:
            if req_arg not in self.arguments:
                missing_args.add(req_arg)
    
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)