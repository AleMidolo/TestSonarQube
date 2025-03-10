def validate_min_max_args(self, args):
    """
    Verifica se il valore degli argomenti è compreso tra i valori minimo e massimo.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise AttributeError("L'oggetto deve avere attributi 'min_value' e 'max_value' definiti.")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            return False
    return True