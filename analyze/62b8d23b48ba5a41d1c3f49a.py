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
                key += tuple(type(arg) for arg in args)
                if kwargs:
                    key += tuple(type(v) for v in kwargs.values())
            return hash(key)

        def wrapper(*args, **kwargs):
            key = make_key(*args, **kwargs)
            
            # Si el resultado está en caché, actualizar orden y retornar
            if key in cache:
                # Mover la clave al final (más recientemente usado)
                order.remove(key)
                order.append(key)
                return cache[key]
            
            # Calcular nuevo resultado
            result = func(*args, **kwargs)
            
            # Si el caché está lleno, eliminar el elemento más recientemente usado
            if len(cache) >= maxsize:
                # Eliminar el último elemento (MRU)
                old_key = order.pop()
                del cache[old_key]
            
            # Almacenar nuevo resultado
            cache[key] = result
            order.append(key)
            
            return result
            
        return wrapper
    
    # Si maxsize es None, no hay límite en el caché
    if maxsize is None:
        maxsize = float('inf')
        
    return decorator