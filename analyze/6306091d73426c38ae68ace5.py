def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        included_groups = parser_dict['include']
        if isinstance(included_groups, list):
            for group in included_groups:
                if group in parser_dict:
                    parser_dict.update(parser_dict[group])
        elif isinstance(included_groups, str):
            if included_groups in parser_dict:
                parser_dict.update(parser_dict[included_groups])
    return parser_dict