def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora
    que guarda los resultados en una caché.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Obtener la caché para esta instancia
            cache_dict = cache(self)
            
            if cache_dict is None:
                # Si no hay caché, ejecutar el método directamente
                return method(self, *args, **kwargs)
                
            # Generar la clave para los argumentos
            k = key(args, kwargs)
            
            try:
                # Intentar obtener el resultado de la caché
                if lock is not None:
                    with lock:
                        return cache_dict[k]
                else:
                    return cache_dict[k]
                    
            except KeyError:
                # Si no está en caché, calcular y guardar
                result = method(self, *args, **kwargs)
                
                if lock is not None:
                    with lock:
                        cache_dict[k] = result
                else:
                    cache_dict[k] = result
                    
                return result
                
        return wrapper
        
    return decorator