import os
import yaml

def get_plugin_spec_flatten_dict(plugin_dir):
    plugin_spec = {}
    
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(plugin_dir, filename), 'r') as file:
                content = yaml.safe_load(file)
                if isinstance(content, dict):
                    for key, value in content.items():
                        plugin_spec[key] = value
    
    return plugin_spec