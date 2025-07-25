def validate_choices_args(self, args):  
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.  

    :param args: Los argumentos recibidos.  
    """
    available_choices = getattr(self, 'available_choices', [])
    if not isinstance(args, list):
        args = [args]
    for arg in args:
        if arg not in available_choices:
            raise ValueError(f"'{arg}' no es una opción válida. Opciones disponibles: {available_choices}")