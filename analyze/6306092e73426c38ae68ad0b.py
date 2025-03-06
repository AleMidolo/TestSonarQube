def validate_min_max_args(self, args):
    """
    Verifica se il valore degli argomenti è compreso tra i valori minimo e massimo.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise AttributeError("min_value and max_value must be defined in the class.")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            raise ValueError(f"Argument {arg} is not between {self.min_value} and {self.max_value}.")
    return True