def get_spec_defaults(self):
    """
    Risolvere i valori degli argomenti dal file di specifica e da altre fonti.
    """
    # Assuming self.spec is a dictionary or similar structure that holds the specification
    defaults = {}
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if isinstance(value, dict) and 'default' in value:
                defaults[key] = value['default']
            else:
                defaults[key] = value
    return defaults