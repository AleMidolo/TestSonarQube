import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
    """
    flat_dict = {}
    
    # प्लगइन स्पेसिफिकेशन फ़ाइल का पथ
    spec_file_path = os.path.join(plugin_dir, 'plugin_spec.json')
    
    if not os.path.exists(spec_file_path):
        raise FileNotFoundError(f"Plugin specification file not found at {spec_file_path}")
    
    with open(spec_file_path, 'r') as file:
        spec_data = json.load(file)
    
    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    flat_dict = flatten_dict(spec_data)
    
    return flat_dict