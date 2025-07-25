def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Return attribute names and descriptions defined by interface.
    if not all:
    Return attribute names and descriptions defined by interface.
    """
    if all:
        return {attr: getattr(self, attr).__doc__ for attr in dir(self) if not attr.startswith('_')}
    else:
        return {attr: getattr(self, attr).__doc__ for attr in dir(self) if not attr.startswith('_') and self.is_defined(attr)}