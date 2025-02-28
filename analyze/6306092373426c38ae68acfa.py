def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    for arg in self.spec.get('arguments', []):
        if 'default' in arg:
            defaults[arg['name']] = arg['default']
    return defaults