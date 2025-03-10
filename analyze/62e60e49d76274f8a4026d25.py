from functools import wraps

def unit_of_work(metadata=None, timeout=None):
    """
    Esta función es un decorador para funciones de transacción que permite un control adicional sobre cómo se lleva a cabo la transacción.

    :param metadata: Un diccionario con metadatos.
    :type metadata: dict
    :param timeout: El tiempo de espera de la transacción en segundos.
    :type timeout: float o None
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Aquí se podría agregar lógica para manejar los metadatos y el timeout
            # Por ejemplo, podríamos pasar estos parámetros a la transacción
            # En este ejemplo, simplemente llamamos a la función original
            return func(*args, **kwargs)
        return wrapper
    return decorator