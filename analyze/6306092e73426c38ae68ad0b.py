def validate_min_max_args(self, args):
    """
    Verifica si el valor de los argumentos está entre los valores mínimo y máximo.

    :param args: Los argumentos recibidos.
    """
    min_value = getattr(self, 'min_value', None)
    max_value = getattr(self, 'max_value', None)
    
    if min_value is not None and max_value is not None:
        for arg in args:
            if not (min_value <= arg <= max_value):
                raise ValueError(f"El valor {arg} no está entre {min_value} y {max_value}.")
    else:
        raise AttributeError("Los atributos 'min_value' y 'max_value' no están definidos.")