def cached(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere una funzione con un callable di memoizzazione che salva  
    i risultati in una cache.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Genera la chiave per la cache
            cache_key = key(*args, **kwargs)
            # Controlla se il risultato è già nella cache
            if cache_key in cache:
                return cache[cache_key]
            # Se non è nella cache, chiama la funzione
            result = func(*args, **kwargs)
            # Salva il risultato nella cache
            cache[cache_key] = result
            return result
        return wrapper
    return decorator