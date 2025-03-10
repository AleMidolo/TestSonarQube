def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if 'include' in parser_dict:
        for group_name in parser_dict['include']:
            if group_name in self.groups:
                parser_dict.update(self.groups[group_name])
            else:
                raise ValueError(f"Group '{group_name}' not found in groups definition.")
    return parser_dict