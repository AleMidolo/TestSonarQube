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
                # Si typed=True, incluir los tipos en la clave
                key += str(tuple(type(arg) for arg in args))
                key += str(tuple(type(val) for val in kwargs.values()))
                
            # Verificar si el resultado está en cache
            if key in cache:
                # Mover el item al final (más recientemente usado)
                cache.move_to_end(key)
                return cache[key]
                
            # Calcular resultado
            result = func(*args, **kwargs)
            
            # Agregar a cache
            cache[key] = result
            
            # Si excede maxsize, eliminar el elemento menos usado
            if len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Agregar métodos para acceder a la cache
        wrapper.cache_info = lambda: cache
        wrapper.cache_clear = lambda: cache.clear()
        
        return wrapper
        
    # Si se usa sin paréntesis
    if callable(maxsize):
        func, maxsize = maxsize, 128
        return decorator(func)
        
    return decorator