def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora  
    que guarda los resultados en una caché.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Generar la clave de caché
            cache_key = key(*args, **kwargs)
            # Intentar obtener el resultado de la caché
            if cache_key in cache:
                return cache[cache_key]
            # Si no está en caché, llamar al método y guardar el resultado
            with (lock if lock else dummy_lock):
                result = func(*args, **kwargs)
                cache[cache_key] = result
            return result
        return wrapper
    return decorator

# Dummy lock for cases where no lock is provided
class dummy_lock:
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        pass