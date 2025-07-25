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
                
    # Get defaults from function signature if available
    if hasattr(self, 'func'):
        sig = inspect.signature(self.func)
        for name, param in sig.parameters.items():
            if param.default is not inspect.Parameter.empty:
                defaults[name] = param.default
                
    return defaults