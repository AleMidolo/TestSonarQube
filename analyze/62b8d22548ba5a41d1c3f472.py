def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorador para envolver un método de clase o de instancia con una función memoizadora
    que guarda los resultados en una caché.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Obtener la caché específica de la instancia/clase
            cache_attr = cache(self)
            
            # Generar la clave para los argumentos
            k = key(method, args, kwargs)
            
            try:
                # Intentar obtener el resultado de la caché
                with lock(self) if lock is not None else nullcontext():
                    result = cache_attr[k]
                return result
            except KeyError:
                # Si no está en caché, calcular y almacenar
                result = method(self, *args, **kwargs)
                with lock(self) if lock is not None else nullcontext():
                    cache_attr[k] = result
                return result
            except TypeError:
                # Si la clave no es hasheable, ejecutar sin caché
                return method(self, *args, **kwargs)
                
        return wrapper
    return decorator