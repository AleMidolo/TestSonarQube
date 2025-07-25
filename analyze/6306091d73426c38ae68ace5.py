def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if 'include' in parser_dict:
        for group in parser_dict['include']:
            if group in self.groups:
                self.groups[group].update(parser_dict['include'][group])
            else:
                self.groups[group] = parser_dict['include'][group]
    return self.groups