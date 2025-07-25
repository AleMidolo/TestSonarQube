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
                # Incluir los tipos si typed=True
                key += tuple(type(arg) for arg in args)
                key += tuple(type(v) for v in kwargs.values())
            return hash(key)

        def wrapper(*args, **kwargs):
            key = make_key(*args, **kwargs)
            
            try:
                # Si el resultado está en caché, moverlo al final (más reciente)
                result = cache[key]
                order.remove(key)
                order.append(key)
                return result
            except KeyError:
                # Calcular nuevo resultado
                result = func(*args, **kwargs)
                
                # Si alcanzamos el tamaño máximo, eliminar el más reciente
                if len(cache) >= maxsize:
                    oldest = order.pop()
                    del cache[oldest]
                
                # Almacenar nuevo resultado
                cache[key] = result
                order.append(key)
                return result
                
        return wrapper
    return decorator