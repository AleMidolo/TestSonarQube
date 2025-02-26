def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    # Assuming self.spec is a dictionary containing the default values
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if isinstance(value, dict) and 'default' in value:
                defaults[key] = value['default']
            elif isinstance(value, list) and value:
                defaults[key] = value[0]  # Assuming the first item is the default
            else:
                defaults[key] = value
    # Additional logic to resolve defaults from other sources can be added here
    return defaults