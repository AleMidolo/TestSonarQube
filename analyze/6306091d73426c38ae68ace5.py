def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    if 'include' in parser_dict:
        for group_name in parser_dict['include']:
            if group_name in self.groups:
                for key, value in self.groups[group_name].items():
                    if key not in parser_dict:
                        parser_dict[key] = value
    return parser_dict