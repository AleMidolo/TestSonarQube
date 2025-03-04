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
        # Dizionario per tenere traccia dell'ordine di inserimento per ogni frequenza
        freq_list = defaultdict(list)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crea la chiave della cache
            if typed:
                key = (*args, *[(k, type(v), v) for k, v in sorted(kwargs.items())])
            else:
                key = (*args, *sorted(kwargs.items()))
                
            try:
                key = hash(key)
            except TypeError:
                # Se la chiave non è hashable, esegui la funzione senza cache
                return func(*args, **kwargs)
                
            # Se il risultato è già in cache
            if key in cache:
                # Aggiorna le frequenze
                old_freq = frequencies[key]
                frequencies[key] += 1
                new_freq = frequencies[key]
                
                # Aggiorna le liste di frequenza
                freq_list[old_freq].remove(key)
                if not freq_list[old_freq]:
                    del freq_list[old_freq]
                freq_list[new_freq].append(key)
                
                return cache[key]
                
            # Se la cache è piena, rimuovi l'elemento meno frequentemente usato
            if maxsize > 0 and len(cache) >= maxsize:
                # Trova la frequenza minima
                min_freq = min(freq_list.keys())
                # Rimuovi il primo elemento con quella frequenza (LRU tra quelli con stessa frequenza)
                lfu_key = freq_list[min_freq].pop(0)
                if not freq_list[min_freq]:
                    del freq_list[min_freq]
                del cache[lfu_key]
                del frequencies[lfu_key]
                
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Memorizza il nuovo risultato
            if maxsize != 0:
                cache[key] = result
                frequencies[key] = 1
                freq_list[1].append(key)
                
            return result
            
        # Aggiungi metodi per accedere alle informazioni della cache
        wrapper.cache_info = lambda: {
            'hits': sum(frequencies.values()) - len(frequencies),
            'misses': len(frequencies),
            'maxsize': maxsize,
            'currsize': len(cache)
        }
        wrapper.cache_clear = lambda: (cache.clear(), frequencies.clear(), freq_list.clear())
        
        return wrapper
        
    return decorator