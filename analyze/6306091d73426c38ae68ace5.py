def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if not isinstance(parser_dict, dict):
        return parser_dict

    if 'include' in parser_dict:
        included_groups = parser_dict['include']
        if isinstance(included_groups, str):
            included_groups = [included_groups]
            
        for group in included_groups:
            if group in self.groups:
                parser_dict.update(self.groups[group])
        
        del parser_dict['include']
        
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            parser_dict[key] = self._include_groups(value)
        elif isinstance(value, list):
            parser_dict[key] = [self._include_groups(item) if isinstance(item, dict) else item 
                              for item in value]
            
    return parser_dict