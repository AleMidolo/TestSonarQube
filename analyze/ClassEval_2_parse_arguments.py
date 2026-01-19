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
    import re
    parts = re.split('\\s+', command_string)
    parts = parts[2:]
    missing_args = set()
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
        else:
            key = part
            value = True
        key = key.lstrip('-')
        if key in self.types:
            value = self._convert_type(key, value)
        self.arguments[key] = value
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)