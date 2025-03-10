def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if not isinstance(parser_dict, dict):
        raise ValueError("parser_dict must be a dictionary")
    
    include_groups = parser_dict.get("include", [])
    if not isinstance(include_groups, list):
        raise ValueError("include must be a list")
    
    for group in include_groups:
        if not isinstance(group, dict):
            raise ValueError("Each include group must be a dictionary")
        
        # Process each group as needed
        # Example: self._process_group(group)