def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No se han definido opciones de elección en la clase.")
    
    if not isinstance(args, (list, tuple)):
        args = [args]
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"El argumento '{arg}' no es una opción válida. Opciones disponibles: {self.choices}")
    
    return True