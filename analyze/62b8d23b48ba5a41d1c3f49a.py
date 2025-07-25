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
        
        def make_key(args, kwargs):
            # Crear una clave única para los argumentos
            key = (args, frozenset(kwargs.items()))
            if typed:
                # Si typed=True, incluir los tipos en la clave
                key += tuple(type(arg) for arg in args)
                key += tuple(type(v) for v in kwargs.values())
            return hash(key)
        
        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            
            try:
                # Si el resultado está en caché, actualizar orden y retornar
                result = cache[key]
                order.remove(key)
                order.append(key)
                return result
            except KeyError:
                # Calcular nuevo resultado
                result = func(*args, **kwargs)
                
                # Si el caché está lleno, eliminar el elemento más recientemente usado
                if len(cache) >= maxsize:
                    old_key = order.pop()
                    del cache[old_key]
                
                # Almacenar nuevo resultado
                cache[key] = result
                order.append(key)
                return result
                
        # Agregar atributos útiles al wrapper
        wrapper.cache_info = lambda: {
            'hits': len(order),
            'misses': func.__code__.co_firstlineno,
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = lambda: cache.clear() or order.clear()
        
        return wrapper
    return decorator