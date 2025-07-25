def get_spec_defaults(self):
    """
    Resolve arguments' values from spec and other sources.
    """
    defaults = {}
    
    if hasattr(self, 'spec') and self.spec:
        # Get default values from spec
        for param_name, param in self.spec.parameters.items():
            if param.default is not param.empty:
                defaults[param_name] = param.default
                
    # Get defaults from class/instance attributes if they exist
    if hasattr(self, 'defaults'):
        defaults.update(self.defaults)
        
    # Get defaults from environment variables if configured
    if hasattr(self, 'env_defaults'):
        for key, env_var in self.env_defaults.items():
            value = os.environ.get(env_var)
            if value is not None:
                defaults[key] = value
                
    return defaults