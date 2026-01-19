import json
import os

def process_json(self, file_path, remove_key):
    """
    read a JSON file and process the data by removing a specified key and rewrite the modified data back to the file.

    :param file_path: str, the path of the JSON file.
    :param remove_key: str, the key to be removed.
    :return: 1, if the specified key is successfully removed and the data is written back.
                0, if the file does not exist or the specified key does not exist in the data.
    >>> json.read_json('test.json')
    {'key1': 'value1', 'key2': 'value2'}
    >>> json.process_json('test.json', 'key1')
    1
    >>> json.read_json('test.json')
    {'key2': 'value2'}
    """
    # Check if file exists
    if not os.path.exists(file_path):
        return 0
    
    try:
        # Read the JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Check if the key exists in the data
        if remove_key not in data:
            return 0
        
        # Remove the specified key
        del data[remove_key]
        
        # Write the modified data back to the file
        with open(file_path, 'w') as f:
            json.dump(data, f)
        
        return 1
    
    except (json.JSONDecodeError, IOError):
        return 0