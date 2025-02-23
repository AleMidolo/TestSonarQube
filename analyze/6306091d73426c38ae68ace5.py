def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    included_groups = {}
    for key, value in parser_dict.items():
        if isinstance(value, dict) and 'include' in value:
            included_groups[key] = self._process_inclusion(value['include'])
        else:
            included_groups[key] = value
    return included_groups

def _process_inclusion(self, include_path):
    # Simulate processing the inclusion from the specified path
    # This is a placeholder for the actual inclusion logic
    return f"Inclusion processed for {include_path}"