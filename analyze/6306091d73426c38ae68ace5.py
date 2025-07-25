def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    if not isinstance(parser_dict, dict):
        return parser_dict

    if 'include' in parser_dict:
        included_groups = parser_dict.pop('include')
        if not isinstance(included_groups, list):
            included_groups = [included_groups]
            
        for group in included_groups:
            if group in self.groups:
                parser_dict.update(self.groups[group])
            else:
                raise ValueError(f"Group '{group}' referenced in include directive not found")
                
    return parser_dict