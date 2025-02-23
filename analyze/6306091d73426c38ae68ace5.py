def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if 'include' in parser_dict:
        include_dict = parser_dict['include']
        for key, value in include_dict.items():
            if key not in parser_dict:
                parser_dict[key] = value
    return parser_dict