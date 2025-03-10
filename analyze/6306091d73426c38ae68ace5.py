def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    if 'include' in parser_dict:
        for include_path in parser_dict['include']:
            with open(include_path, 'r') as file:
                included_data = file.read()
                # Aquí puedes procesar included_data según sea necesario
                # Por ejemplo, podrías parsearlo y combinarlo con parser_dict
                # Este es un ejemplo básico, ajusta según tus necesidades
                parser_dict.update(eval(included_data))
    return parser_dict