def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if 'include' in parser_dict:
        for group_name in parser_dict['include']:
            if group_name in self.groups:
                included_group = self.groups[group_name]
                for key, value in included_group.items():
                    if key not in parser_dict:
                        parser_dict[key] = value
                    elif isinstance(value, dict) and isinstance(parser_dict[key], dict):
                        parser_dict[key].update(value)
                    elif isinstance(value, list) and isinstance(parser_dict[key], list):
                        parser_dict[key].extend(value)
    return parser_dict