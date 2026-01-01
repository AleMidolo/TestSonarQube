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
    self.arguments = {}
    tokens = command_string.split()
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.startswith('--') and '=' in token:
            arg_name = token[2:].split('=')[0]
            arg_value = token.split('=', 1)[1]
            if arg_name in self.types:
                self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
            else:
                self.arguments[arg_name] = arg_value
        elif token.startswith('--'):
            arg_name = token[2:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                arg_value = tokens[i + 1]
                if arg_name in self.types:
                    self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                else:
                    self.arguments[arg_name] = arg_value
                i += 1
            else:
                self.arguments[arg_name] = True
        elif token.startswith('-') and (not token.startswith('--')):
            arg_name = token[1:]
            if i + 1 < len(tokens) and (not tokens[i + 1].startswith('-')):
                arg_value = tokens[i + 1]
                if arg_name in self.types:
                    self.arguments[arg_name] = self._convert_type(arg_name, arg_value)
                else:
                    self.arguments[arg_name] = arg_value
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