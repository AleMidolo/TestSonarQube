def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("L'oggetto non ha un attributo 'choices' definito.")
    
    if not isinstance(self.choices, (list, tuple)):
        raise TypeError("L'attributo 'choices' deve essere una lista o una tupla.")
    
    if args not in self.choices:
        raise ValueError(f"L'argomento '{args}' non è tra le opzioni valide: {self.choices}")
    
    return True