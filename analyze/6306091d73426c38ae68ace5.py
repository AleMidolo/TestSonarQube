def _include_groups(self, parser_dict):
    """
    Resuelve la directiva de inclusión del diccionario en los archivos de especificación.
    """
    # Assuming parser_dict is a dictionary that contains 'include' key with a list of groups to include
    if 'include' in parser_dict:
        included_groups = parser_dict['include']
        # Logic to include the specified groups
        # This could involve merging or updating the parser_dict with the included groups
        # For example:
        for group in included_groups:
            if group in self.available_groups:  # Assuming self.available_groups is a list of all available groups
                parser_dict.update(self.available_groups[group])
            else:
                raise ValueError(f"Group '{group}' not found in available groups.")
    return parser_dict