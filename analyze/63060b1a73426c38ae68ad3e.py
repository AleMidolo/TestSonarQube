def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    flattened_dict = {}
    
    try:
        # Read and parse plugin spec file
        spec_file = os.path.join(plugin_dir, 'plugin.spec')
        if not os.path.exists(spec_file):
            return flattened_dict
            
        with open(spec_file, 'r') as f:
            spec_data = yaml.safe_load(f)
            
        def flatten(data, parent_key=''):
            items = []
            for key, value in data.items():
                new_key = f"{parent_key}.{key}" if parent_key else key
                
                if isinstance(value, dict):
                    items.extend(flatten(value, new_key).items())
                else:
                    items.append((new_key, value))
            return dict(items)
            
        flattened_dict = flatten(spec_data)
        
    except Exception as e:
        # Return empty dict if any error occurs
        pass
        
    return flattened_dict