def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    defaults = {}
    
    # Get defaults from spec if available
    if hasattr(self, 'spec') and self.spec:
        for param in self.spec.parameters.values():
            if param.default != param.empty:
                defaults[param.name] = param.default
                
    # Get defaults from other sources like config files
    if hasattr(self, 'config'):
        defaults.update(self.config.get('defaults', {}))
        
    # Get defaults from instance attributes
    for attr in dir(self):
        if attr.startswith('default_'):
            param_name = attr[8:] # Remove 'default_' prefix
            defaults[param_name] = getattr(self, attr)
            
    return defaults