def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No choices defined for validation.")
    
    if args not in self.choices:
        raise ValueError(f"Invalid choice: {args}. Valid choices are: {self.choices}")
    
    return True