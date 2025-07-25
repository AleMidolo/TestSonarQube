def lfu_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memoizzazione
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Frequently Used (LFU).
    """
    from collections import defaultdict
    from functools import wraps
    
    def decorator(func):
        # Cache per memorizzare i risultati
        cache = {}
        # Contatore delle frequenze di utilizzo
        frequencies = defaultdict(int)
        # Dizionario per tenere traccia dell'ordine di inserimento
        insertion_order = {}
        counter = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            
            # Crea la chiave della cache
            if typed:
                key = (*args, *[(k, type(v), v) for k, v in sorted(kwargs.items())])
            else:
                key = (*args, *sorted(kwargs.items()))
                
            try:
                # Se il risultato è già in cache
                result = cache[key]
                # Incrementa la frequenza
                frequencies[key] += 1
                return result
            except KeyError:
                # Calcola il nuovo risultato
                result = func(*args, **kwargs)
                
                # Se la cache è piena, rimuovi l'elemento meno frequentemente usato
                if len(cache) >= maxsize:
                    # Trova la frequenza minima
                    min_freq = min(frequencies.values())
                    # Trova tutti gli elementi con frequenza minima
                    min_freq_keys = [k for k, v in frequencies.items() if v == min_freq]
                    # Rimuovi l'elemento più vecchio tra quelli con frequenza minima
                    oldest_key = min(
                        min_freq_keys,
                        key=lambda k: insertion_order[k]
                    )
                    del cache[oldest_key]
                    del frequencies[oldest_key]
                    del insertion_order[oldest_key]
                
                # Aggiungi il nuovo risultato alla cache
                cache[key] = result
                frequencies[key] = 1
                insertion_order[key] = counter
                counter += 1
                
                return result
                
        # Aggiungi metodi per accedere alla cache
        wrapper.cache_info = lambda: {
            'hits': sum(frequencies.values()) - len(frequencies),
            'misses': len(frequencies),
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = lambda: (cache.clear(), frequencies.clear(), insertion_order.clear())
        
        return wrapper
    
    return decorator