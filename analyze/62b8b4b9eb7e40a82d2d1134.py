def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Return attribute names and descriptions defined by interface."""
    if not all:
        return {name: desc for name, desc in self.__class__.__dict__.items() if not name.startswith('__')}
    return {name: desc for name, desc in self.__class__.__dict__.items()}