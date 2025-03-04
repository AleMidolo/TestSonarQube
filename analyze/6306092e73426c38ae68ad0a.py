def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.  

    :param args: Los argumentos recibidos.  
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'_{arg_name}_choices'):
            choices = getattr(self, f'_{arg_name}_choices')
            if arg_value not in choices:
                raise ValueError(f"Invalid value '{arg_value}' for argument '{arg_name}'. "
                               f"Valid choices are: {choices}")