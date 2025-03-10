def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if not isinstance(parser_dict, dict):
        raise ValueError("parser_dict must be a dictionary")
    
    include_groups = parser_dict.get("include", {})
    if not isinstance(include_groups, dict):
        raise ValueError("include key must be a dictionary")
    
    for group_name, group_value in include_groups.items():
        if not isinstance(group_value, (list, str)):
            raise ValueError(f"Value for group '{group_name}' must be a list or string")
        
        if isinstance(group_value, str):
            include_groups[group_name] = [group_value]
    
    return include_groups