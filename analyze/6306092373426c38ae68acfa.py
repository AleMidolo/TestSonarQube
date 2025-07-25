def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    defaults = {}
    # Assuming self.spec is a dictionary or object that contains default values
    if hasattr(self, 'spec'):
        if isinstance(self.spec, dict):
            for key, value in self.spec.items():
                if isinstance(value, dict) and 'default' in value:
                    defaults[key] = value['default']
                elif hasattr(value, 'default'):
                    defaults[key] = value.default
        elif hasattr(self.spec, 'defaults'):
            defaults = self.spec.defaults
    return defaults