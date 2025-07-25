import os
import json

def get_plugin_spec_flatten_dict(plugin_dir):
    """
    Creates a flat dict from the plugin spec

    :param plugin_dir: A path to the plugin's dir
    :return: A flatten dictionary contains the plugin's properties
    """
    flatten_dict = {}

    for root, _, files in os.walk(plugin_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        data = json.load(f)
                        for key, value in data.items():
                            flatten_dict[key] = value
                    except json.JSONDecodeError:
                        continue

    return flatten_dict