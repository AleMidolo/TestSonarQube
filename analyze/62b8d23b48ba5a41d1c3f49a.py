def mru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto richiamabile che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo di tipo Most Recently Used (MRU).
    """
    def decorator(func):
        # Dictionary per memorizzare i risultati della cache
        cache = {}
        # Lista per tenere traccia dell'ordine di utilizzo
        order = []
        
        def wrapper(*args, **kwargs):
            # Crea una chiave per la cache basata sugli argomenti
            if typed:
                key = (*args, *kwargs.items(), *[type(arg) for arg in args])
            else:
                key = (*args, *kwargs.items())
                
            try:
                # Se il risultato è già in cache
                result = cache[key]
                # Aggiorna l'ordine MRU
                order.remove(key)
                order.append(key)
                return result
            except KeyError:
                # Calcola il nuovo risultato
                result = func(*args, **kwargs)
                
                # Se la cache è piena, rimuovi l'elemento usato meno recentemente
                if len(cache) >= maxsize:
                    # Rimuovi l'elemento più vecchio
                    oldest = order.pop(0)
                    del cache[oldest]
                
                # Aggiungi il nuovo risultato alla cache
                cache[key] = result
                order.append(key)
                return result
                
        wrapper.cache_info = lambda: {
            'maxsize': maxsize,
            'currsize': len(cache),
            'cache': cache,
            'order': order
        }
        
        wrapper.cache_clear = lambda: (cache.clear(), order.clear())
        
        return wrapper
    
    # Se maxsize è None, non usare la cache
    if maxsize is None:
        return lambda func: func
        
    return decorator