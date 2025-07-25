def _include_groups(self, parser_dict):
    """
    स्पेक फाइलों में 'include dict' निर्देश को हल करता है।
    """
    if not isinstance(parser_dict, dict):
        raise ValueError("parser_dict must be a dictionary")
    
    include_dict = parser_dict.get("include", {})
    if not isinstance(include_dict, dict):
        raise ValueError("'include' key must map to a dictionary")
    
    for group_name, group_value in include_dict.items():
        if not isinstance(group_value, (list, str)):
            raise ValueError(f"Group '{group_name}' must be a list or string")
        
        if isinstance(group_value, str):
            include_dict[group_name] = [group_value]
    
    return include_dict