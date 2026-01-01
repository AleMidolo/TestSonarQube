def get_argument(self, key):
    """
        Recupera il valore dell'argomento specificato dal dizionario degli argomenti e lo restituisce.
        :param key: str, nome dell'argomento
        :return: Il valore dell'argomento, o None se l'argomento non esiste.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
    return self.arguments.get(key)