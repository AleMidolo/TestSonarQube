def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ 
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
    """
    flattened_dict = {}
    
    def flatten(d, parent_key=''):
        for key, value in d.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            
            if isinstance(value, dict):
                flatten(value, new_key)
            else:
                flattened_dict[new_key] = value
                
    try:
        # Read plugin specification file
        spec_file = os.path.join(plugin_dir, 'plugin.json')
        if not os.path.exists(spec_file):
            spec_file = os.path.join(plugin_dir, 'plugin.yaml')
            
        if os.path.exists(spec_file):
            # Load specification based on file extension
            if spec_file.endswith('.json'):
                with open(spec_file) as f:
                    spec = json.load(f)
            else:
                with open(spec_file) as f:
                    spec = yaml.safe_load(f)
                    
            # Flatten the specification dictionary
            flatten(spec)
            
    except Exception as e:
        print(f"Error reading plugin specification: {str(e)}")
        return {}
        
    return flattened_dict