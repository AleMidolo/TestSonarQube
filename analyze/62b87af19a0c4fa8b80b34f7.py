def difference(d1, d2, level=-1):
    """
    Return a dictionary with items from *d1* not contained in *d2*.

    *level* sets the maximum depth of recursion. For infinite recursion,
    set that to -1. For level 1,
    if a key is present both in *d1* and *d2* but has different values,
    it is included into the difference.
    See :func:`intersection` for more details.

    *d1* and *d2* remain unchanged. However, *d1* or some of its
    subdictionaries may be returned directly.
    Make a deep copy of the result when appropriate.

    .. versionadded:: 0.5
       add keyword argument *level*.
    """
    if level == 0:
        return {}

    diff = {}
    for key, value in d1.items():
        if key not in d2:
            diff[key] = value
        elif isinstance(value, dict) and isinstance(d2[key], dict) and level != 1:
            sub_diff = difference(value, d2[key], level - 1 if level != -1 else -1)
            if sub_diff:
                diff[key] = sub_diff
        elif value != d2[key]:
            diff[key] = value

    return diff