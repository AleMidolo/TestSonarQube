def lru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo Least Recently Used (LRU).
    """
    def decorator(func):
        # Dictionary per memorizzare i risultati della cache
        cache = {}
        # Lista per tenere traccia dell'ordine di utilizzo
        order = []
        
        def wrapper(*args, **kwargs):
            # Crea una chiave univoca per gli argomenti
            key = str(args) + str(kwargs)
            if typed:
                # Se typed=True, include i tipi degli argomenti nella chiave
                key += str([type(arg) for arg in args])
                key += str({k: type(v) for k, v in kwargs.items()})
            
            # Se il risultato è già in cache, aggiorna l'ordine e restituiscilo
            if key in cache:
                # Aggiorna l'ordine di utilizzo
                order.remove(key)
                order.append(key)
                return cache[key]
            
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Se la cache è piena, rimuovi l'elemento meno recentemente usato
            if len(cache) >= maxsize:
                oldest_key = order.pop(0)
                del cache[oldest_key]
            
            # Aggiungi il nuovo risultato alla cache
            cache[key] = result
            order.append(key)
            
            return result
            
        # Aggiungi attributi utili al wrapper
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'hits': sum(1 for k in order if k in cache),
            'misses': sum(1 for k in order if k not in cache)
        }
        wrapper.cache_clear = lambda: cache.clear() and order.clear()
        
        return wrapper
    
    # Se viene chiamato direttamente con una funzione
    if callable(maxsize):
        func = maxsize
        maxsize = 128
        return decorator(func)
    
    return decorator