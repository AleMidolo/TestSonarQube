from collections import defaultdict
from functools import wraps
import time

def lfu_cache(maxsize=128, typed=False):
    def decorator(func):
        # Diccionarios para almacenar el caché y contadores
        cache = {}
        frequency = defaultdict(int)
        last_access = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crear clave para el caché
            if typed:
                key = (*args, *sorted(kwargs.items()), *[type(arg) for arg in args])
            else:
                key = (*args, *sorted(kwargs.items()))

            # Si el resultado está en caché, incrementar frecuencia y retornar
            if key in cache:
                frequency[key] += 1
                last_access[key] = time.time()
                return cache[key]

            # Si el caché está lleno, eliminar el elemento menos frecuente
            if len(cache) >= maxsize:
                min_freq = min(frequency.values())
                # Obtener elementos con la frecuencia mínima
                min_freq_keys = [k for k, v in frequency.items() if v == min_freq]
                # Si hay varios con la misma frecuencia, eliminar el menos usado recientemente
                lru_key = min(min_freq_keys, key=lambda k: last_access[k])
                
                del cache[lru_key]
                del frequency[lru_key]
                del last_access[lru_key]

            # Calcular nuevo resultado y almacenarlo
            result = func(*args, **kwargs)
            cache[key] = result
            frequency[key] = 1
            last_access[key] = time.time()

            return result

        # Agregar método para limpiar el caché
        def clear_cache():
            cache.clear()
            frequency.clear()
            last_access.clear()

        wrapper.clear_cache = clear_cache
        return wrapper

    return decorator