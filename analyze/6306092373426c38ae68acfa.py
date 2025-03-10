def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if hasattr(value, 'default'):
                defaults[key] = value.default
    return defaults