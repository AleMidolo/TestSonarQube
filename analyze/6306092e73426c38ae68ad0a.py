def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No 'choices' attribute defined for validation.")
    
    if args not in self.choices:
        raise ValueError(f"Invalid argument: {args}. Expected one of {self.choices}.")
    
    return True