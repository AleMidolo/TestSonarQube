def get_spec_defaults(self):
    """
    Resolver los valores de los argumentos desde la especificación y otras fuentes.
    """
    # Assuming self.spec is a dictionary or similar structure that holds the specification
    defaults = {}
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if isinstance(value, dict) and 'default' in value:
                defaults[key] = value['default']
    return defaults