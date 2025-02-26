def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    # Assuming self.spec is a dictionary containing the specifications
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if isinstance(value, dict) and 'default' in value:
                defaults[key] = value['default']
            elif isinstance(value, list) and value:
                defaults[key] = value[0]  # Taking the first element as default
            else:
                defaults[key] = value  # Fallback to the value itself if no default is specified

    # Additional sources can be checked here, e.g., environment variables, config files, etc.
    
    return defaults