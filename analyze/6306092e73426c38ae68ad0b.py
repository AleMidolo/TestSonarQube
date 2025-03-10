def validate_min_max_args(self, args):
    """
    Verifica si el valor de los argumentos está entre los valores mínimo y máximo.

    :param args: Los argumentos recibidos.
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise AttributeError("El objeto no tiene definidos los atributos 'min_value' y 'max_value'.")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            return False
    return True