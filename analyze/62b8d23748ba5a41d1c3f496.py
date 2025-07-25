def lfu_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable di memoizzazione
    che salva fino a `maxsize` risultati basandosi su un algoritmo Least Frequently Used (LFU).
    """
    def decorator(func):
        # Dictionary per memorizzare i risultati della cache
        cache = {}
        # Dictionary per tenere traccia della frequenza di utilizzo
        freq = {}
        # Counter per l'ordine di inserimento
        counter = 0
        
        def wrapper(*args, **kwargs):
            nonlocal counter
            
            # Crea una chiave per la cache basata sugli argomenti
            if typed:
                key = (*args, *[(k, type(v), v) for k, v in sorted(kwargs.items())])
            else:
                key = (*args, *[(k, v) for k, v in sorted(kwargs.items())])
                
            # Se il risultato è già in cache, incrementa la frequenza e restituisci
            if key in cache:
                freq[key] += 1
                return cache[key]
            
            # Calcola il nuovo risultato
            result = func(*args, **kwargs)
            
            # Se la cache è piena, rimuovi l'elemento meno frequentemente usato
            if len(cache) >= maxsize:
                # Trova la frequenza minima
                min_freq = min(freq.values())
                # Trova tutti gli elementi con frequenza minima
                min_freq_keys = [k for k, v in freq.items() if v == min_freq]
                # Rimuovi il primo elemento inserito tra quelli con frequenza minima
                lfu_key = min_freq_keys[0]
                del cache[lfu_key]
                del freq[lfu_key]
            
            # Aggiungi il nuovo risultato alla cache
            cache[key] = result
            freq[key] = 1
            counter += 1
            
            return result
            
        return wrapper
    
    return decorator