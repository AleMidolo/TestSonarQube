def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        from functools import wraps
        from collections import OrderedDict
        
        # Cache que almacena los resultados
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crear clave de cache
            key = str(args) + str(kwargs)
            if typed:
                key += str([type(arg) for arg in args])
                key += str([type(val) for val in kwargs.values()])
                
            # Verificar si el resultado está en cache
            if key in cache:
                # Mover el item al final (más recientemente usado)
                cache.move_to_end(key)
                return cache[key]
                
            # Calcular resultado
            result = func(*args, **kwargs)
            
            # Agregar a cache
            if maxsize > 0:
                # Si cache está lleno, remover el item menos usado
                if len(cache) >= maxsize:
                    cache.popitem(last=False)
                cache[key] = result
                
            return result
            
        # Agregar métodos de utilidad
        wrapper.cache_info = lambda: {
            "hits": len(cache),
            "maxsize": maxsize,
            "currsize": len(cache)
        }
        wrapper.cache_clear = cache.clear
        
        return wrapper
        
    # Si se usa sin parámetros
    if callable(maxsize):
        func, maxsize = maxsize, 128
        return decorator(func)
        
    return decorator