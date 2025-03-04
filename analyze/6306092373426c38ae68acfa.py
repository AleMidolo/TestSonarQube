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
                
        # Get values from environment variables if specified
        if hasattr(self.spec, 'env_vars'):
            for param_name, env_var in self.spec.env_vars.items():
                if env_var in os.environ:
                    defaults[param_name] = os.environ[env_var]
                    
        # Get values from config file if specified
        if hasattr(self.spec, 'config_file') and os.path.exists(self.spec.config_file):
            with open(self.spec.config_file) as f:
                config = json.load(f)
                for param_name in self.spec.parameters:
                    if param_name in config:
                        defaults[param_name] = config[param_name]
                        
    return defaults