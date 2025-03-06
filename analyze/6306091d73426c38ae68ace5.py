def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        for include_key in parser_dict['include']:
            if include_key in parser_dict:
                parser_dict[include_key].update(parser_dict['include'][include_key])
            else:
                parser_dict[include_key] = parser_dict['include'][include_key]
        del parser_dict['include']
    return parser_dict