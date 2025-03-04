def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ 
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
    """
    flattened_dict = {}
    
    try:
        # Read and parse plugin specification file
        spec_file = os.path.join(plugin_dir, 'plugin.json')
        with open(spec_file, 'r', encoding='utf-8') as f:
            spec = json.load(f)
            
        def flatten(d, parent_key=''):
            for key, value in d.items():
                new_key = f"{parent_key}.{key}" if parent_key else key
                
                if isinstance(value, dict):
                    flatten(value, new_key)
                else:
                    flattened_dict[new_key] = value
                    
        flatten(spec)
        
    except FileNotFoundError:
        print(f"Plugin specification file not found in {plugin_dir}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in plugin specification file")
    except Exception as e:
        print(f"Error processing plugin specification: {str(e)}")
        
    return flattened_dict