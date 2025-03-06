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
        def wrapper(tx, *args, **kwargs):
            # Aplicar metadatos si se proporcionan
            if metadata is not None:
                tx.run("CALL dbms.setTXMetaData($metadata)", metadata=metadata)
            
            # Aplicar timeout si se proporciona
            if timeout is not None:
                tx.run("CALL dbms.setTransactionTimeout($timeout)", timeout=timeout)
            
            # Ejecutar la función de transacción
            return func(tx, *args, **kwargs)
        return wrapper
    return decorator