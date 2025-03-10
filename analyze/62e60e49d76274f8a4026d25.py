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
            # Aquí se puede agregar lógica adicional para manejar metadata y timeout
            # Por ejemplo, se podría pasar metadata y timeout a la transacción
            # en el contexto de Neo4j.
            if metadata is not None:
                kwargs['metadata'] = metadata
            if timeout is not None:
                kwargs['timeout'] = timeout
            return func(*args, **kwargs)
        return wrapper
    return decorator