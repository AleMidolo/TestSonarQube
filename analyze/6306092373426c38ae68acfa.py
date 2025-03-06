def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    # Assuming self.spec is a dictionary or similar structure that holds the default values
    defaults = {}
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if isinstance(value, dict) and 'default' in value:
                defaults[key] = value['default']
            else:
                defaults[key] = value
    return defaults