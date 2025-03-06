def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No 'choices' attribute defined for validation.")
    
    if not isinstance(self.choices, (list, tuple, set)):
        raise TypeError("'choices' must be a list, tuple, or set.")
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Valid choices are: {self.choices}")