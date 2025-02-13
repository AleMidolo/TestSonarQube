def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        for group in parser_dict['include']:
            if group in self.groups:
                parser_dict.update(self.groups[group])
            else:
                raise KeyError(f"Group '{group}' not found in available groups.")
    return parser_dict