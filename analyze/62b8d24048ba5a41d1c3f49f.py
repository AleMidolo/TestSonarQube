from functools import wraps
from collections import OrderedDict
import time

def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
    def decorator(func):
        # Cache che memorizza i risultati e i timestamp
        cache = OrderedDict()
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crea la chiave della cache
            key = (*args, *(kwargs.items()))
            if typed:
                key += tuple(type(arg) for arg in args)
                key += tuple(type(val) for val in kwargs.values())
            
            # Ottiene il timestamp corrente
            now = timer()
            
            # Rimuove le entry scadute
            expired = []
            for k, (val, timestamp) in cache.items():
                if now - timestamp > ttl:
                    expired.append(k)
            for k in expired:
                cache.pop(k)
                
            # Controlla se il risultato è in cache e non scaduto
            if key in cache:
                val, timestamp = cache[key]
                if now - timestamp <= ttl:
                    # Sposta l'elemento in fondo (LRU)
                    cache.move_to_end(key)
                    return val
                else:
                    # Rimuove l'elemento scaduto
                    cache.pop(key)
            
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Aggiunge il risultato alla cache
            cache[key] = (result, now)
            
            # Rimuove gli elementi più vecchi se la cache supera maxsize
            while len(cache) > maxsize:
                cache.popitem(last=False)
                
            return result
            
        # Aggiunge metodi per gestire la cache
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'ttl': ttl,
            'current_size': len(cache)
        }
        wrapper.cache_clear = cache.clear
        
        return wrapper
    return decorator