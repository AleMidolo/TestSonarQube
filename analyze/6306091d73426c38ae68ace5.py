def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    if 'include' in parser_dict:
        for include_key in parser_dict['include']:
            if include_key in parser_dict:
                parser_dict.update(parser_dict[include_key])
        del parser_dict['include']
    return parser_dict