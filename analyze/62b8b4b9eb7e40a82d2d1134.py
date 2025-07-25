def namesAndDescriptions(self, all=False): # pylint:disable=redefined-builtin
    """Return attribute names and descriptions defined by interface.
    if not all:

    Return attribute names and descriptions defined by interface.
    """
    attrs = {}
    for name, desc in self.getDescriptionFor():
        if all or not name.startswith('_'):
            attrs[name] = desc
    return attrs