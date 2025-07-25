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
    # Aquí se implementaría la lógica para procesar la inclusión
    # Por ejemplo, cargar un archivo o un grupo de configuraciones
    return {}  # Retornar un diccionario vacío como un ejemplo