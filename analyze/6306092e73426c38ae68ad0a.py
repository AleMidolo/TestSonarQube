def validate_choices_args(self, args):
    """
    Verifica si el valor de los argumentos de elección es una de las opciones disponibles.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No 'choices' attribute found in the class.")
    
    if not isinstance(self.choices, (list, tuple)):
        raise TypeError("'choices' must be a list or tuple.")
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Valid choices are: {self.choices}")
    
    return True