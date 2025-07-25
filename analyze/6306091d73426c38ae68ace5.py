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
                        included_content = self._parse_yaml(f)
                        result[key] = included_content
                except FileNotFoundError:
                    raise FileNotFoundError(f"Include file not found: {include_file}")
            else:
                result[key] = self._include_groups(value)
        else:
            result[key] = value
            
    return result