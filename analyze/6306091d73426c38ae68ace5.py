def _include_groups(self, parser_dict):
    """
    Risolve la direttiva "include dict" nei file di specifica
    """
    if 'include' in parser_dict:
        included_groups = parser_dict['include']
        if isinstance(included_groups, list):
            for group in included_groups:
                if group in self.groups:
                    parser_dict.update(self.groups[group])
        elif included_groups in self.groups:
            parser_dict.update(self.groups[included_groups])
    return parser_dict