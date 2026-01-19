def add_argument(self, arg, required=False, arg_type=str):
    """
        Aggiunge un argomento a self.types e self.required.
        Controlla se si tratta di un argomento obbligatorio e memorizza il tipo di argomento.
        Se l'argomento è impostato come obbligatorio, verrà aggiunto a "required".
        Il tipo e il nome dell'argomento sono memorizzati nel dizionario types come coppie chiave-valore.
        :param arg: str, nome dell'argomento
        :param required: bool, se l'argomento è obbligatorio, il valore predefinito è False
        :param arg_type: str, tipo di argomento, il valore predefinito è str
        >>> parser.add_argument('arg1', True, 'int')
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'int'}
        """
    self.types[arg] = arg_type
    if required:
        self.required.add(arg)