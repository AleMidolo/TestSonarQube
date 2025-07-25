def names(self, all=False): # pylint:disable=redefined-builtin
    """Return the attribute names defined by the interface.
    if not all:

    Return the attribute names defined by the interface.
    """
    if all:
        # Return all attribute names including inherited ones
        return list(self.__dict__.keys())
    else:
        # Return only directly defined attribute names
        return [name for name in self.__dict__.keys() 
                if not name.startswith('_')]