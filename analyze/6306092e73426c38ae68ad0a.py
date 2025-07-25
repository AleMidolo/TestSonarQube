def validate_choices_args(self, args):
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.  

    :param args: Gli argomenti ricevuti.  
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'_{arg_name}_choices'):
            choices = getattr(self, f'_{arg_name}_choices')
            if arg_value not in choices:
                raise ValueError(f"Invalid value '{arg_value}' for argument '{arg_name}'. "
                               f"Valid choices are: {choices}")