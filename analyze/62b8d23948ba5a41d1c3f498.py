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
            cache[key] = result
            
            # Remover el elemento menos usado si se excede maxsize
            if maxsize and len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Agregar métodos de utilidad
        wrapper.cache_info = lambda: {
            'hits': sum(1 for _ in cache),
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = cache.clear
        
        return wrapper
        
    # Si se usa directamente como @lru_cache
    if callable(maxsize):
        func, maxsize = maxsize, 128
        return decorator(func)
        
    return decorator