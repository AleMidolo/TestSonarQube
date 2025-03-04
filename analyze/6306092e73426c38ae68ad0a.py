def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.  

    :param args: Los argumentos recibidos.  
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, 'choices') and arg_name in self.choices:
            valid_choices = self.choices[arg_name]
            if arg_value not in valid_choices:
                raise ValueError(f"El valor '{arg_value}' no es válido para el argumento '{arg_name}'. "
                               f"Las opciones válidas son: {valid_choices}")