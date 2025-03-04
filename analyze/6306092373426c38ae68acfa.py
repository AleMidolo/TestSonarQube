def get_spec_defaults(self):
    """
    Risolvere i valori degli argomenti dal file di specifica e da altre fonti.
    """
    spec_defaults = {}
    
    # Check if spec file exists
    if hasattr(self, 'spec_file') and self.spec_file:
        try:
            # Read spec file
            with open(self.spec_file, 'r') as f:
                spec_data = f.read()
                
            # Parse spec file data
            for line in spec_data.splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        spec_defaults[key] = value
                    except ValueError:
                        continue
                        
        except (IOError, OSError):
            # Handle file read errors
            pass
            
    # Add any other sources of defaults
    if hasattr(self, 'env_defaults'):
        spec_defaults.update(self.env_defaults)
        
    if hasattr(self, 'config_defaults'):
        spec_defaults.update(self.config_defaults)
        
    return spec_defaults