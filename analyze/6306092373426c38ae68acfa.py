def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    defaults = {}
    # Assuming 'self.spec' contains the specifications from which to extract defaults
    if hasattr(self, 'spec'):
        for arg in self.spec.get('args', []):
            if 'default' in arg:
                defaults[arg['name']] = arg['default']
    
    # Assuming 'self.sources' contains other sources to extract defaults
    if hasattr(self, 'sources'):
        for source in self.sources:
            for arg in source.get('args', []):
                if 'default' in arg and arg['name'] not in defaults:
                    defaults[arg['name']] = arg['default']
    
    return defaults