def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora  
    que guarda los resultados en una caché.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Generar la clave de caché
            cache_key = key(self, *args, **kwargs)
            # Intentar obtener el resultado de la caché
            with lock:
                if cache_key in cache:
                    return cache[cache_key]
            # Llamar al método original
            result = func(self, *args, **kwargs)
            # Almacenar el resultado en la caché
            with lock:
                cache[cache_key] = result
            return result
        return wrapper
    return decorator