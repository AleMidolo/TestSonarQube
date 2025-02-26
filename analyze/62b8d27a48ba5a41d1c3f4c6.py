def cached(cache, key=hashkey, lock=None):
    """
    Decorador para envolver una función con una llamada que memoriza y guarda  
    los resultados en una caché.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Generar la clave de caché
            cache_key = key(*args, **kwargs)
            # Intentar obtener el resultado de la caché
            with (lock if lock else dummy_lock):
                if cache_key in cache:
                    return cache[cache_key]
            # Llamar a la función y almacenar el resultado en la caché
            result = func(*args, **kwargs)
            with (lock if lock else dummy_lock):
                cache[cache_key] = result
            return result
        return wrapper
    return decorator