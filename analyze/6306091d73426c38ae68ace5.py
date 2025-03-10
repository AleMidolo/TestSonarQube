def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            self._include_groups(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    self._include_groups(item)
        # Aquí puedes agregar la lógica específica para manejar la inclusión de grupos
        # dependiendo de la estructura de tu diccionario y los archivos de especificación.