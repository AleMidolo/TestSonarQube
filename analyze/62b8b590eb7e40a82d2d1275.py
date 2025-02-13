def _legacy_mergeOrderings(orderings):
    seen = set()
    result = []
    
    for ordering in orderings:
        for item in ordering:
            if item not in seen:
                seen.add(item)
                result.append(item)
    
    return result