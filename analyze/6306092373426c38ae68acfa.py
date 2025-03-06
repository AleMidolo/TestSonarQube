def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    # Assuming `self.spec` is a dictionary or similar structure that holds the default values
    defaults = {}
    if hasattr(self, 'spec'):
        for key, value in self.spec.items():
            if 'default' in value:
                defaults[key] = value['default']
    return defaults