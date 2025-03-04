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
    if hasattr(self, 'env_defaults') and self.env_defaults:
        import os
        for key, env_var in self.env_defaults.items():
            if env_var in os.environ:
                defaults[key] = os.environ[env_var]
                
    return defaults