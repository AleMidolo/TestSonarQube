def _dictsum(dicts):
    """
    पुनरावृत्तीय dicts द्वारा प्रदान किए गए शब्दकोशों के मानों को संयोजित करें।

    >>> _dictsum([{'a': 1, 'b': 2}, {'a': 5, 'b': 0}])
    {'a': 6, 'b': 2}
    """
    if not dicts:
        return {}
        
    result = {}
    for d in dicts:
        for key, value in d.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
                
    return result