def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("El objeto no tiene un atributo 'choices' definido.")
    
    if not isinstance(self.choices, (list, tuple)):
        raise TypeError("El atributo 'choices' debe ser una lista o tupla.")
    
    if not args:
        raise ValueError("No se proporcionaron argumentos para validar.")
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"El argumento '{arg}' no es una opción válida. Opciones disponibles: {self.choices}")
    
    return True