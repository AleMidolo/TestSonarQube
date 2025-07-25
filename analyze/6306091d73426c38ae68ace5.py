def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    if 'include' not in parser_dict:
        return parser_dict

    include_dict = parser_dict['include']
    if not isinstance(include_dict, dict):
        raise ValueError("The 'include' directive must be a dictionary.")

    for key, value in include_dict.items():
        if key in parser_dict:
            if isinstance(parser_dict[key], dict) and isinstance(value, dict):
                parser_dict[key].update(value)
            else:
                parser_dict[key] = value
        else:
            parser_dict[key] = value

    del parser_dict['include']
    return parser_dict