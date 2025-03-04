def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante 
    che salva i risultati in una cache.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            # Genera la chiave per la cache
            k = key(self, *args, **kwargs)
            
            # Se è specificato un lock, lo acquisisce
            if lock is not None:
                lock.acquire()
                
            try:
                # Prova a recuperare il risultato dalla cache
                return cache[k]
            except KeyError:
                # Se non presente in cache, calcola il risultato
                result = method(self, *args, **kwargs)
                cache[k] = result
                return result
            finally:
                # Rilascia il lock se presente
                if lock is not None:
                    lock.release()
                    
        return wrapper
    return decorator