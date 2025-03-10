def _include_groups(self, parser_dict):
    """
    Resolves the include dict directive in the spec files.
    """
    if not isinstance(parser_dict, dict):
        return parser_dict

    if 'include' in parser_dict:
        include_key = parser_dict['include']
        if include_key in self.spec:
            included_dict = self.spec[include_key]
            if isinstance(included_dict, dict):
                # Merge the included dict with the current dict, giving precedence to the current dict
                merged_dict = {**included_dict, **parser_dict}
                # Remove the 'include' key as it's no longer needed
                merged_dict.pop('include', None)
                return merged_dict
        else:
            raise ValueError(f"Include key '{include_key}' not found in spec.")

    # Recursively apply to nested dictionaries
    for key, value in parser_dict.items():
        if isinstance(value, dict):
            parser_dict[key] = self._include_groups(value)
        elif isinstance(value, list):
            parser_dict[key] = [self._include_groups(item) if isinstance(item, dict) else item for item in value]

    return parser_dict