def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    # Implementation to resolve 'include dict' directive in spec files
    for key, value in parser_dict.items():
        if isinstance(value, dict) and 'include' in value:
            include_key = value['include']
            if include_key in parser_dict:
                parser_dict[key] = parser_dict[include_key]
            else:
                raise KeyError(f"Include key '{include_key}' not found in parser_dict")
    return parser_dict