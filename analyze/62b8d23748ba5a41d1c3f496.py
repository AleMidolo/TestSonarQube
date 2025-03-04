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
        min_freq = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crea una chiave unica per gli argomenti
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
                freq_list[old_freq].remove(key)
                if not freq_list[old_freq] and old_freq == min_freq:
                    min_freq += 1
                freq_list[old_freq + 1].append(key)
                return cache[key]
                
            # Se la cache è piena, rimuovi l'elemento meno frequentemente usato
            if maxsize and len(cache) >= maxsize:
                # Trova la chiave da rimuovere (LFU)
                lfu_key = freq_list[min_freq].pop(0)
                del cache[lfu_key]
                del frequencies[lfu_key]
                if not freq_list[min_freq]:
                    del freq_list[min_freq]
                    
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Aggiungi il nuovo risultato alla cache
            cache[key] = result
            frequencies[key] = 1
            freq_list[1].append(key)
            min_freq = 1
            
            return result
            
        # Aggiungi attributi utili al wrapper
        wrapper.cache_info = lambda: cache
        wrapper.cache_clear = lambda: (cache.clear(), frequencies.clear(), freq_list.clear())
        
        return wrapper
        
    return decorator