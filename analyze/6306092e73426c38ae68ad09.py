def validate_length_args(self, args):
    """
    Verifica si el valor de los argumentos no supera la longitud especificada.

    :param args: Los argumentos recibidos.
    """
    max_length = 100  # Longitud máxima permitida
    for arg in args:
        if len(str(arg)) > max_length:
            raise ValueError(f"El argumento {arg} supera la longitud máxima permitida de {max_length} caracteres.")
    return True