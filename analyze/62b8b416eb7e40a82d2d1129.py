def names(self, all=False): # pylint:disable=redefined-builtin
    """Return the attribute names defined by the interface.
    if not all:
        Return the attribute names defined by the interface.
    """
    if all:
        return [attr for attr in dir(self) if not attr.startswith('_')]
    else:
        return [attr for attr in dir(self) if not attr.startswith('_') and not callable(getattr(self, attr))]