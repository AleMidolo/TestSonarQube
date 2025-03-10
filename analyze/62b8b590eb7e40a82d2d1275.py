def _legacy_mergeOrderings(orderings):
    """
    Unisci più ordinamenti in modo che l'ordine all'interno di ciascun ordinamento venga preservato.

    Gli ordinamenti sono vincolati in modo tale che, se un oggetto appare in due o più ordinamenti, il suffisso che inizia con l'oggetto deve essere presente in entrambi gli ordinamenti.

    Ad esempio:

    >>> _mergeOrderings([
    ... ['x', 'y', 'z'],
    ... ['q', 'z'],
    ... [1, 3, 5],
    ... ['z']
    ... ])
    ['x', 'y', 'q', 1, 3, 5, 'z']
    """
    merged = []
    for ordering in orderings:
        for item in ordering:
            if item not in merged:
                merged.append(item)
    return merged