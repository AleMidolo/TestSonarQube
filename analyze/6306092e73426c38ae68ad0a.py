def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No 'choices' attribute defined in the class.")
    
    for arg_name, arg_value in args.items():
        if arg_name in self.choices:
            if arg_value not in self.choices[arg_name]:
                raise ValueError(f"Invalid value '{arg_value}' for argument '{arg_name}'. Valid options are: {self.choices[arg_name]}")