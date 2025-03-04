def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ 
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
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
        # Try to read plugin specification file
        spec_file = f"{plugin_dir}/plugin.json"
        with open(spec_file, 'r') as f:
            import json
            plugin_spec = json.load(f)
            
        # Flatten the dictionary
        flatten_dict(plugin_spec)
        
    except FileNotFoundError:
        print(f"Plugin specification file not found in {plugin_dir}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in plugin specification file")
    except Exception as e:
        print(f"Error processing plugin specification: {str(e)}")
        
    return flattened_dict