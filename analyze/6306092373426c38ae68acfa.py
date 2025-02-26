def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    # Assuming self.spec is a dictionary containing the default values
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if value is not None:
                defaults[key] = value

    # You can add more sources to resolve defaults if needed
    # For example, checking environment variables or configuration files

    return defaults