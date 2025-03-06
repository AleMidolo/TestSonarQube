from functools import lru_cache as _lru_cache

def lru_cache(maxsize=128, typed=False):
    """
    Decorator per racchiudere una funzione con un oggetto callable che memorizza
    fino a `maxsize` risultati basandosi su un algoritmo Least Recently Used (LRU).
    """
    return _lru_cache(maxsize=maxsize, typed=typed)