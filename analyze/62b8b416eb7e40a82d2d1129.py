def names(self, all=False): # pylint:disable=redefined-builtin
        """Return the attribute names defined by the interface."""
        if not all:
            return [attr for attr in dir(self) if not attr.startswith('__')]
        return dir(self)