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
            if cache_key in cache:
                return cache[cache_key]
            # Si no está en caché, llamar a la función
            result = func(*args, **kwargs)
            # Guardar el resultado en la caché
            cache[cache_key] = result
            return result
        return wrapper
    return decorator