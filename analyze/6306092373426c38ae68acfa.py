def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    defaults = {}
    
    # Get defaults from spec if available
    if hasattr(self, 'spec') and self.spec:
        for param in self.spec.parameters:
            if param.default is not None:
                defaults[param.name] = param.default
                
    # Get defaults from other sources like config files
    if hasattr(self, 'config'):
        defaults.update(self.config.get('defaults', {}))
        
    # Get defaults from environment variables
    for key, value in os.environ.items():
        if key.startswith(self.env_prefix):
            param_name = key[len(self.env_prefix):].lower()
            defaults[param_name] = value
            
    return defaults