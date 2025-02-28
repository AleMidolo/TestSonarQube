def names(self, all=False):  # pylint:disable=redefined-builtin
    """Return the attribute names defined by the interface.
    
    Args:
        all (bool): If True, return all attribute names, including private ones.
                   If False, return only public attribute names.
    
    Returns:
        list: A list of attribute names.
    """
    if all:
        return [name for name in dir(self) if not name.startswith('__')]
    else:
        return [name for name in dir(self) if not name.startswith('_')]