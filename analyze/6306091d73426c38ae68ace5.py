def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    include_dict = parser_dict.get('include', {})
    for key, value in include_dict.items():
        if isinstance(value, dict):
            self._include_groups(value)
        else:
            # Process the include value as needed
            self.process_include(key, value)