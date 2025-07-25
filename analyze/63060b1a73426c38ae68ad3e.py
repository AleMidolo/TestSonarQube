def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    flattened_dict = {}
    
    def flatten_dict(d, parent_key=''):
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten_dict(value, new_key)
            else:
                flattened_dict[new_key] = value
    
    try:
        # Try to read and parse the plugin spec file
        spec_file = os.path.join(plugin_dir, 'plugin.spec')
        if not os.path.exists(spec_file):
            return {}
            
        with open(spec_file, 'r') as f:
            spec_data = yaml.safe_load(f)
            
        if not spec_data or not isinstance(spec_data, dict):
            return {}
            
        # Flatten the dictionary
        flatten_dict(spec_data)
        
        return flattened_dict
        
    except (yaml.YAMLError, IOError):
        return {}