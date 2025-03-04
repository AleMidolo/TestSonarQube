def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    if not parser_dict:
        return {}
        
    result = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            if '@include' in value:
                include_file = value['@include']
                try:
                    with open(include_file, 'r') as f:
                        included_dict = json.load(f)
                    result[key] = self._include_groups(included_dict)
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error including file {include_file}: {str(e)}")
                    result[key] = value
            else:
                result[key] = self._include_groups(value)
        else:
            result[key] = value
            
    return result