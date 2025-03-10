def namesAndDescriptions(self, all=False):  # pylint:disable=redefined-builtin
    """Return attribute names and descriptions defined by interface.
    
    Args:
        all (bool): If True, return all attributes. If False, return only specific attributes.
    
    Returns:
        dict: A dictionary where keys are attribute names and values are their descriptions.
    """
    attributes = {}
    for name, value in self.__dict__.items():
        if not all and not name.startswith('_'):
            attributes[name] = value.__doc__ if value.__doc__ else "No description available."
        elif all:
            attributes[name] = value.__doc__ if value.__doc__ else "No description available."
    return attributes