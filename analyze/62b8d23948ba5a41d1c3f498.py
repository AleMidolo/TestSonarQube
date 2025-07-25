from functools import lru_cache as _lru_cache

def lru_cache(maxsize=128, typed=False):
    """
    Decorador para envolver una función con un objeto invocable que memoriza
    hasta `maxsize` resultados basados en un algoritmo de Menor Recientemente Usado (LRU, por sus siglas en inglés).
    """
    return _lru_cache(maxsize=maxsize, typed=typed)