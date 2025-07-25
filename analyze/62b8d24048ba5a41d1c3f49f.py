from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Cache para almacenar resultados y timestamps
        cache = OrderedDict()
        hits = misses = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            
            # Crear clave para el cache
            key = str(args)
            if kwargs:
                key += str(sorted(kwargs.items()))
            if typed:
                key += str(tuple(type(arg) for arg in args))
                if kwargs:
                    key += str(tuple(type(v) for v in kwargs.values()))
                    
            now = timer()
            
            # Verificar si la clave existe y no ha expirado
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp <= ttl:
                    hits += 1
                    # Mover el elemento al final (más recientemente usado)
                    cache.move_to_end(key)
                    return result
                else:
                    # Eliminar entrada expirada
                    del cache[key]
            
            # Cache miss - calcular nuevo resultado
            misses += 1
            result = func(*args, **kwargs)
            
            # Agregar nuevo resultado al cache
            cache[key] = (result, now)
            
            # Eliminar entradas más antiguas si se excede maxsize
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Agregar funciones auxiliares al wrapper
        def cache_info():
            return {
                'hits': hits,
                'misses': misses,
                'maxsize': maxsize,
                'currsize': len(cache),
                'ttl': ttl
            }
            
        def cache_clear():
            nonlocal hits, misses
            cache.clear()
            hits = misses = 0
            
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear
        return wrapper
        
    return decorator