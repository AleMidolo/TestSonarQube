def cachedmethod(cache, key=hashkey, lock=None):
    """
    Decorator per racchiudere un metodo di classe o di istanza con una funzione memoizzante che salva i risultati in una cache.

    :param cache: La cache in cui memorizzare i risultati.
    :param key: Funzione per generare la chiave di cache. Default è hashkey.
    :param lock: Lock opzionale per sincronizzare l'accesso alla cache.
    :return: Il metodo decorato con la funzionalità di caching.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            cache_key = key(self, *args, **kwargs)
            if lock:
                with lock:
                    if cache_key in cache:
                        return cache[cache_key]
                    result = method(self, *args, **kwargs)
                    cache[cache_key] = result
                    return result
            else:
                if cache_key in cache:
                    return cache[cache_key]
                result = method(self, *args, **kwargs)
                cache[cache_key] = result
                return result
        return wrapper
    return decorator