def _dictsum(dicts):
    """
    Combina i valori dei dizionari forniti tramite l'iterabile `dicts`.

    >>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
    {'a': 6, 'b': 2}
    """
    from collections import defaultdict

    result = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            result[key] += value
            
    return dict(result)