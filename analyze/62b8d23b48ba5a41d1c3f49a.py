def mru_cache(maxsize=128, typed=False):
    """
    Decorador para envolver una función con un objeto invocable que memoriza hasta `maxsize` resultados 
    basados en un algoritmo de Más Recientemente Usado (MRU).
    """
    def decorator(func):
        # Diccionario para almacenar el caché
        cache = {}
        # Lista para mantener el orden de uso
        order = []
        
        def wrapper(*args, **kwargs):
            # Crear clave para el caché
            if typed:
                key = (args, tuple(sorted(kwargs.items())), tuple(type(arg) for arg in args))
            else:
                key = (args, tuple(sorted(kwargs.items())))
                
            # Verificar si el resultado está en caché
            if key in cache:
                # Actualizar orden de uso
                order.remove(key)
                order.append(key)
                return cache[key]
                
            # Calcular resultado
            result = func(*args, **kwargs)
            
            # Si el caché está lleno, eliminar el elemento más recientemente usado
            if len(cache) >= maxsize:
                oldest_key = order.pop()
                del cache[oldest_key]
                
            # Almacenar nuevo resultado
            cache[key] = result
            order.append(key)
            
            return result
            
        # Agregar atributos para acceder al caché
        wrapper.cache_info = lambda: {'hits': len(order), 'maxsize': maxsize, 'currsize': len(cache)}
        wrapper.cache_clear = lambda: (cache.clear(), order.clear())
        
        return wrapper
        
    return decorator