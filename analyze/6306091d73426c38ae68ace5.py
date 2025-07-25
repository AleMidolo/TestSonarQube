def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if not isinstance(parser_dict, dict):
        raise ValueError("parser_dict must be a dictionary")
    
    include_groups = parser_dict.get("include", {})
    if not isinstance(include_groups, dict):
        raise ValueError("include must be a dictionary")
    
    result = {}
    for key, value in include_groups.items():
        if not isinstance(value, (list, str)):
            raise ValueError(f"include value for key '{key}' must be a list or string")
        
        if isinstance(value, str):
            result[key] = [value]
        else:
            result[key] = value
    
    return result