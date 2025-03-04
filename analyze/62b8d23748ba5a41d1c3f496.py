from collections import defaultdict
from functools import wraps
import time

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Diccionarios para almacenar el caché y contadores
        cache = {}
        frequency = defaultdict(int)
        last_used = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crear clave para el caché
            if typed:
                key = (*args, *sorted(kwargs.items()), *[type(arg) for arg in args])
            else:
                key = (*args, *sorted(kwargs.items()))
                
            try:
                key = hash(key)
            except TypeError:
                # Si la clave no es hasheable, ejecutar sin caché
                return func(*args, **kwargs)
                
            # Verificar si está en caché
            if key in cache:
                frequency[key] += 1
                last_used[key] = time.time()
                return cache[key]
                
            # Si el caché está lleno, eliminar el elemento menos frecuente
            if len(cache) >= maxsize:
                min_freq = min(frequency.values())
                # Obtener elementos con frecuencia mínima
                min_freq_keys = [k for k, v in frequency.items() if v == min_freq]
                # Si hay varios con misma frecuencia, eliminar el menos usado
                lru_key = min(min_freq_keys, key=lambda k: last_used[k])
                
                del cache[lru_key]
                del frequency[lru_key]
                del last_used[lru_key]
                
            # Calcular nuevo valor y almacenar en caché
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            last_used[key] = time.time()
            
            return result
            
        # Agregar métodos para acceder al estado del caché
        wrapper.cache_info = lambda: {
            'hits': sum(frequency.values()) - len(frequency),
            'misses': len(frequency),
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = lambda: (cache.clear(), frequency.clear(), last_used.clear())
        
        return wrapper
    return decorator