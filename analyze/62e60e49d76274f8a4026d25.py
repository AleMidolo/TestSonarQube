def unit_of_work(metadata=None, timeout=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Aquí se implementaría la lógica para manejar la transacción
            # y aplicar los metadatos y el tiempo de espera.
            # Este es un ejemplo simplificado.
            if timeout is not None:
                # Configurar el tiempo de espera de la transacción
                pass  # Lógica para establecer el timeout

            if metadata is not None:
                # Adjuntar metadatos a la transacción
                pass  # Lógica para establecer los metadatos

            # Ejecutar la función de transacción
            result = func(*args, **kwargs)
            return result

        return wrapper
    return decorator