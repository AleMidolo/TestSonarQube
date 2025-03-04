def names(self, all=False): # pylint:disable=redefined-builtin
    """Return the attribute names defined by the interface.
    if not all:

    Return the attribute names defined by the interface.
    """
    if all:
        return list(self._attributes.keys())
    else:
        return [name for name, attr in self._attributes.items() 
                if not attr.is_hidden]