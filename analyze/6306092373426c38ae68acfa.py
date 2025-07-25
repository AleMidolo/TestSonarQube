def get_spec_defaults(self):
    """
    Risolvere i valori degli argomenti dal file di specifica e da altre fonti.
    """
    # Assuming self.spec_file is the path to the specification file
    defaults = {}
    
    try:
        with open(self.spec_file, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    defaults[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Specification file {self.spec_file} not found.")
    
    # Add other sources if needed
    # For example, environment variables or hardcoded defaults
    # defaults.update(os.environ)
    
    return defaults