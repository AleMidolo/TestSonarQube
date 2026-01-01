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
    self.arguments.clear()
    tokens = command_string.split()
    i = 0
    while i < len(tokens) and (tokens[i].endswith('.py') or tokens[i] == 'python'):
        i += 1
    while i < len(tokens):
        token = tokens[i]
        if '=' in token:
            if token.startswith('--') or token.startswith('-'):
                key_value = token.split('=', 1)
                key = key_value[0].lstrip('-')
                value = key_value[1]
                converted_value = self._convert_type(key, value)
                self.arguments[key] = converted_value
            i += 1
        elif token.startswith('--') or token.startswith('-'):
            key = token.lstrip('-')
            if i + 1 < len(tokens) and (not (tokens[i + 1].startswith('--') or tokens[i + 1].startswith('-'))):
                value = tokens[i + 1]
                converted_value = self._convert_type(key, value)
                self.arguments[key] = converted_value
                i += 2
            else:
                self.arguments[key] = True
                i += 1
        else:
            i += 1
    missing_args = self.required - set(self.arguments.keys())
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)