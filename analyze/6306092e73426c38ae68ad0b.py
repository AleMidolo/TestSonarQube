def validate_min_max_args(self, args):
    """
    Verifica si el valor de los argumentos está entre los valores mínimo y máximo.

    :param args: Los argumentos recibidos.
    """
    min_value = 0  # Define el valor mínimo
    max_value = 100  # Define el valor máximo
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"El valor {arg} no está entre {min_value} y {max_value}.")
    
    return True