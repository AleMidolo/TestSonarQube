def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        for include_key in parser_dict['include']:
            if include_key in parser_dict:
                included_dict = parser_dict[include_key]
                for key, value in included_dict.items():
                    if key not in parser_dict:
                        parser_dict[key] = value
                    elif isinstance(value, dict) and isinstance(parser_dict[key], dict):
                        parser_dict[key].update(value)
                    elif isinstance(value, list) and isinstance(parser_dict[key], list):
                        parser_dict[key].extend(value)
        del parser_dict['include']
    return parser_dict