def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
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
        description = getattr(value, '__doc__', 'No description available')
        attributes[name] = description
    return attributes