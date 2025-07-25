def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if not parser_dict:
        return {}
        
    result = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            if 'include' in value:
                # Handle include directive
                include_path = value['include']
                try:
                    with open(include_path, 'r') as f:
                        included_dict = json.load(f)
                    result[key] = self._include_groups(included_dict)
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error including file {include_path}: {str(e)}")
                    result[key] = value
            else:
                # Recursively process nested dictionaries
                result[key] = self._include_groups(value)
        else:
            # Copy non-dictionary values as-is
            result[key] = value
            
    return result