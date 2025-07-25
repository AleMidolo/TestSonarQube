def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    include_dict = parser_dict.get('include', {})
    for group, items in include_dict.items():
        if group not in self.groups:
            self.groups[group] = []
        self.groups[group].extend(items)