from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Cache para almacenar resultados con timestamps
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crear clave para el cache
            key = str(args)
            if kwargs:
                key += str(sorted(kwargs.items()))
            if typed:
                key += str(tuple(type(arg) for arg in args))
                if kwargs:
                    key += str(tuple(type(v) for v in kwargs.values()))
                    
            # Obtener tiempo actual
            current_time = timer()
            
            # Verificar si la clave existe y no ha expirado
            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp <= ttl:
                    # Mover el elemento al final (más recientemente usado)
                    cache.move_to_end(key)
                    return result
                else:
                    # Eliminar entrada expirada
                    del cache[key]
            
            # Calcular nuevo resultado
            result = func(*args, **kwargs)
            
            # Agregar al cache
            cache[key] = (result, current_time)
            
            # Mantener el tamaño máximo del cache
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Agregar método para limpiar el cache
        wrapper.cache_clear = lambda: cache.clear()
        
        # Agregar método para obtener el tamaño del cache
        wrapper.cache_info = lambda: len(cache)
        
        return wrapper
    return decorator