def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        include_dict = parser_dict['include']
        for key, value in include_dict.items():
            if isinstance(value, dict):
                self._include_groups(value)
            else:
                parser_dict[key] = value
    return parser_dict