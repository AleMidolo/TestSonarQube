import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
    """
    spec_file = os.path.join(plugin_dir, 'plugin_spec.json')
    if not os.path.exists(spec_file):
        raise FileNotFoundError(f"Plugin specification file not found in {plugin_dir}")
    
    with open(spec_file, 'r') as file:
        spec_data = json.load(file)
    
    flat_dict = {}
    def flatten(d, parent_key='', sep='.'):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                flatten(v, new_key, sep=sep)
            else:
                flat_dict[new_key] = v
        return flat_dict
    
    return flatten(spec_data)