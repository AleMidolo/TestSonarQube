def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if not isinstance(parser_dict, dict):
        return parser_dict

    if 'include' in parser_dict:
        included_groups = parser_dict['include']
        if not isinstance(included_groups, list):
            included_groups = [included_groups]
            
        result = {}
        for group in included_groups:
            if group in self.groups:
                result.update(self.groups[group])
            
        # Remove the include directive and merge with remaining items
        parser_dict.pop('include')
        result.update(parser_dict)
        return result
        
    return parser_dict