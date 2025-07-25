def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    if not parser_dict:
        return {}
        
    result = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            if '_include' in value:
                include_file = value['_include']
                try:
                    with open(include_file, 'r') as f:
                        included_dict = yaml.safe_load(f)
                    # Merge included dictionary with original values
                    included_dict.update({k:v for k,v in value.items() if k != '_include'})
                    result[key] = self._include_groups(included_dict)
                except (IOError, yaml.YAMLError) as e:
                    raise ValueError(f"Error including file {include_file}: {str(e)}")
            else:
                result[key] = self._include_groups(value)
        else:
            result[key] = value
            
    return result