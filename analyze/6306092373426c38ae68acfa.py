def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    # Assuming 'self.spec' contains the specifications from which defaults can be extracted
    defaults = {}
    if hasattr(self, 'spec'):
        for arg in self.spec.get('args', []):
            if 'default' in arg:
                defaults[arg['name']] = arg['default']
    return defaults