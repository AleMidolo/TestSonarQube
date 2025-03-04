def mru_cache(maxsize=128, typed=False):
    """
    Decorador para envolver una función con un objeto invocable que memoriza hasta `maxsize` resultados 
    basados en un algoritmo de Más Recientemente Usado (MRU).
    """
    def decorator(func):
        # Diccionario para almacenar los resultados cacheados
        cache = {}
        # Lista para mantener el orden de uso
        order = []
        
        def make_key(*args, **kwargs):
            # Crear una clave única para los argumentos
            key = args
            if kwargs:
                key += tuple(sorted(kwargs.items()))
            if typed:
                # Si typed=True, incluir los tipos en la clave
                key += tuple(type(arg) for arg in args)
                key += tuple(type(v) for v in kwargs.values())
            return hash(key)

        def wrapper(*args, **kwargs):
            key = make_key(*args, **kwargs)
            
            if key in cache:
                # Si el resultado está en caché, actualizar orden
                order.remove(key)
                order.append(key)
                return cache[key]
                
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                # Si el caché está lleno, eliminar el elemento más recientemente usado
                old_key = order.pop()
                del cache[old_key]
                
            # Almacenar nuevo resultado
            cache[key] = result
            order.append(key)
            
            return result
            
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'hits': sum(1 for k in order if k in cache),
            'misses': sum(1 for k in order if k not in cache)
        }
        
        wrapper.cache_clear = lambda: cache.clear() or order.clear()
        
        return wrapper
    
    return decorator