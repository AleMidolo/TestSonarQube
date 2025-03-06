def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    if 'include' in parser_dict:
        for include_path in parser_dict['include']:
            with open(include_path, 'r') as file:
                included_data = file.read()
                parser_dict.update(eval(included_data))
        del parser_dict['include']
    return parser_dict