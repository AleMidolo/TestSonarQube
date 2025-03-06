import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    प्लगइन स्पेसिफिकेशन से एक फ्लैट डिक्शनरी बनाता है।

    :param plugin_dir: प्लगइन की डायरेक्टरी का पथ
    :return: एक फ्लैट डिक्शनरी जो प्लगइन की प्रॉपर्टीज़ को समाहित करती है
    """
    plugin_spec_path = os.path.join(plugin_dir, 'plugin_spec.json')
    if not os.path.exists(plugin_spec_path):
        raise FileNotFoundError(f"Plugin specification file not found at {plugin_spec_path}")
    
    with open(plugin_spec_path, 'r') as file:
        plugin_spec = json.load(file)
    
    def flatten_dict(d, parent_key='', sep='.'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
    
    return flatten_dict(plugin_spec)