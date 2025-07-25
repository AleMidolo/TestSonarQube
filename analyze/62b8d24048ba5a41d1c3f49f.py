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
            if typed:
                key += str(type(args))
            if kwargs:
                key += str(sorted(kwargs.items()))
                if typed:
                    key += str(type(kwargs))
                    
            # Obtener tiempo actual
            current_time = timer()
            
            # Limpiar entradas expiradas
            expired = []
            for k, (val, timestamp) in cache.items():
                if current_time - timestamp > ttl:
                    expired.append(k)
            for k in expired:
                cache.pop(k)
                
            # Verificar si el resultado está en cache y no expirado
            if key in cache:
                val, timestamp = cache[key]
                if current_time - timestamp <= ttl:
                    # Mover al final (más recientemente usado)
                    cache.move_to_end(key)
                    return val
                    
            # Calcular nuevo resultado
            result = func(*args, **kwargs)
            
            # Agregar al cache
            cache[key] = (result, current_time)
            
            # Mantener tamaño máximo
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Agregar método para limpiar cache
        wrapper.cache_clear = lambda: cache.clear()
        
        return wrapper
    return decorator