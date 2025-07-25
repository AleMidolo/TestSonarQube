def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.

    :param args: Gli argomenti ricevuti.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No 'choices' attribute found in the class.")
    
    if not isinstance(self.choices, (list, tuple)):
        raise TypeError("'choices' must be a list or tuple.")
    
    if not args:
        raise ValueError("No arguments provided.")
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Valid choices are: {self.choices}")
    
    return True