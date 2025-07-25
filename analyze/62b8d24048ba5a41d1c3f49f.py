from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Cache che memorizza i risultati e i timestamp
        cache = OrderedDict()
        # Cache per i timestamp di scadenza
        expires = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crea la chiave della cache
            key = (*args, *(kwargs.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            
            # Verifica se la chiave è nella cache e non è scaduta
            now = timer()
            try:
                result = cache[key]
                if now < expires[key]:
                    # Sposta l'elemento in fondo (LRU)
                    cache.move_to_end(key)
                    expires.move_to_end(key)
                    return result
                else:
                    # Rimuove l'elemento scaduto
                    del cache[key]
                    del expires[key]
            except KeyError:
                pass
            
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Aggiunge il risultato alla cache
            cache[key] = result
            expires[key] = now + ttl
            
            # Rimuove gli elementi più vecchi se la cache supera maxsize
            while len(cache) > maxsize:
                cache.popitem(last=False)
                expires.popitem(last=False)
                
            return result
            
        # Aggiunge metodi per gestire la cache
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'ttl': ttl,
            'current_size': len(cache)
        }
        wrapper.cache_clear = lambda: (cache.clear(), expires.clear())
        
        return wrapper
    return decorator