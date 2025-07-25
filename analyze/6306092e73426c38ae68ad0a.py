def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.  

    :param args: Gli argomenti ricevuti.  
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, 'choices') and arg_name in self.choices:
            valid_choices = self.choices[arg_name]
            if arg_value not in valid_choices:
                raise ValueError(f"Invalid choice for argument '{arg_name}'. "
                               f"Must be one of: {valid_choices}")