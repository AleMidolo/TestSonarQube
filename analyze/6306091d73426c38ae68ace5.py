def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    included_groups = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict) and 'include' in value:
            included_key = value['include']
            if included_key in parser_dict:
                included_groups[key] = parser_dict[included_key]
            else:
                raise KeyError(f"Included key '{included_key}' not found in parser_dict.")
        else:
            included_groups[key] = value
    return included_groups