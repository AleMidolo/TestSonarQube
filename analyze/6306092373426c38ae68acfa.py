def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    defaults = {}
    # Assuming self.spec is a dictionary or object that contains the default values
    if hasattr(self, 'spec'):
        if isinstance(self.spec, dict):
            defaults.update(self.spec)
        else:
            # If spec is an object, get its attributes
            for key in dir(self.spec):
                if not key.startswith('_'):
                    defaults[key] = getattr(self.spec, key)
    return defaults