def determineMetaclass(bases, explicit_mc=None):
    """
    Determine metaclass from 1+ bases and optional explicit __metaclass__
    """
    if explicit_mc is not None:
        metaclass = explicit_mc
    elif not bases:
        metaclass = type
    else:
        metaclass = type(bases[0])
        for base in bases[1:]:
            if type(base) is not metaclass:
                metaclass = type
                break
    return metaclass