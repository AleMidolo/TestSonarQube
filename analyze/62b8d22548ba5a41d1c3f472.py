def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora
    que guarda los resultados en una caché.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Obtener la caché específica de la instancia/clase
            cache_attr = cache(self)
            
            if cache_attr is None:  # Si no hay caché, ejecutar método sin cachear
                return method(self, *args, **kwargs)
                
            # Generar clave única para los argumentos
            k = key(args, kwargs)
            
            try:
                # Intentar obtener resultado de caché
                if lock is not None:
                    with lock:
                        return cache_attr[k]
                else:
                    return cache_attr[k]
                    
            except KeyError:
                # Si no está en caché, calcular y guardar
                result = method(self, *args, **kwargs)
                
                if lock is not None:
                    with lock:
                        cache_attr[k] = result
                else:
                    cache_attr[k] = result
                    
                return result
                
        return wrapper
        
    return decorator