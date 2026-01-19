def parse_arguments(self, command_string):
    """
    Analizza la stringa di argomenti della riga di comando fornita e invoca _convert_type per memorizzare il risultato analizzato in un tipo specifico nel dizionario degli argomenti.
    Controlla la presenza di argomenti richiesti mancanti, se presenti, e restituisce False con i nomi degli argomenti mancanti, altrimenti restituisce True.
    :param command_string: str, stringa di argomenti della riga di comando, formattata come "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
    :return tuple: (True, None) se l'analisi ha successo, (False, missing_args) se l'analisi fallisce,
        dove missing_args è un insieme dei nomi degli argomenti mancanti che sono str.
    >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
    (True, None)
    >>> parser.arguments
    {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
    """
    # Split the command string into tokens
    tokens = command_string.split()
    
    # Skip the first two tokens (python script.py)
    tokens = tokens[2:] if len(tokens) > 2 else []
    
    # Initialize arguments dictionary
    self.arguments = {}
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # Check if token starts with -- or -
        if token.startswith('--') or token.startswith('-'):
            # Remove leading dashes
            arg_name = token.lstrip('-')
            
            # Check if argument has = format (--arg=value)
            if '=' in arg_name:
                parts = arg_name.split('=', 1)
                arg_name = parts[0]
                value = parts[1]
                self.arguments[arg_name] = self._convert_type(arg_name, value)
                i += 1
            else:
                # Check if next token exists and is not an argument
                if i + 1 < len(tokens) and not tokens[i + 1].startswith('-'):
                    value = tokens[i + 1]
                    self.arguments[arg_name] = self._convert_type(arg_name, value)
                    i += 2
                else:
                    # It's a flag/option (boolean)
                    self.arguments[arg_name] = True
                    i += 1
        else:
            i += 1
    
    # Check for missing required arguments
    if hasattr(self, 'required_args'):
        missing_args = set()
        for req_arg in self.required_args:
            if req_arg not in self.arguments:
                missing_args.add(req_arg)
        
        if missing_args:
            return (False, missing_args)
    
    return (True, None)