def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    # Assuming 'self.spec' contains the specifications
    for key, value in self.spec.items():
        if isinstance(value, dict) and 'default' in value:
            defaults[key] = value['default']
        elif isinstance(value, list) and value:
            defaults[key] = value[0]  # Taking the first value as default
        else:
            defaults[key] = None  # No default found
    return defaults