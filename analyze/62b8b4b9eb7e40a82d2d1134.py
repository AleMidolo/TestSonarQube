def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Return attribute names and descriptions defined by interface.
    
    Args:
        all (bool): If True, return all attributes and descriptions. 
                    If False, return only the non-private attributes and descriptions.
    
    Returns:
        dict: A dictionary where keys are attribute names and values are their descriptions.
    """
    attributes = {}
    for name, value in self.__dict__.items():
        if not all and name.startswith('_'):
            continue
        description = value.__doc__ if hasattr(value, '__doc__') else None
        attributes[name] = description
    return attributes