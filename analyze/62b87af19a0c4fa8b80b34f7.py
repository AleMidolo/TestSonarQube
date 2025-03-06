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
    for key in d1:
        if key not in d2:
            diff[key] = d1[key]
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if level != 1:
                sub_diff = difference(d1[key], d2[key], level - 1 if level != -1 else -1)
                if sub_diff:
                    diff[key] = sub_diff
        elif d1[key] != d2[key]:
            diff[key] = d1[key]

    return diff