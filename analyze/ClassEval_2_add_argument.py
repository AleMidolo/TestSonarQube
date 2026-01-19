def add_argument(self, arg, required=False, arg_type=str):
    """
    Agrega un argumento a self.types y self.required.
    Verifica si es un argumento requerido y almacena el tipo de argumento.
    Si el argumento se establece como requerido, se añadirá al conjunto de requeridos.
    El tipo y el nombre del argumento se almacenan en el diccionario types como pares clave-valor.
    :param arg: str, nombre del argumento
    :param required: bool, si el argumento es requerido, por defecto es False
    :param arg_type: str, tipo de argumento, por defecto es str
    >>> parser.add_argument('arg1', True, 'int')
    >>> parser.required
    {'arg1'}
    >>> parser.types
    {'arg1': 'int'}
    """
    if required:
        self.required.add(arg)
    self.types[arg] = arg_type