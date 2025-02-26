def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora  
    que guarda los resultados en una caché.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # Generar la clave de caché
            cache_key = key(self, *args, **kwargs)
            # Comprobar si el resultado está en la caché
            if cache_key in cache:
                return cache[cache_key]
            # Si no está en la caché, ejecutar el método
            with (lock or dummy_lock):
                result = func(self, *args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator