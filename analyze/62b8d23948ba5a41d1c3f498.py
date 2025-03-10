from functools import lru_cache as _lru_cache

def lru_cache(maxsize=128, typed=False):
    """
    Decorator to wrap a function with a memoizing callable that saves
    up to `maxsize` results based on a Least Recently Used (LRU)
    algorithm.
    """
    return _lru_cache(maxsize=maxsize, typed=typed)