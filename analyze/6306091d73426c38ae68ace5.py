def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if not isinstance(parser_dict, dict):
        return parser_dict
        
    if 'include' not in parser_dict:
        return parser_dict
        
    included_groups = parser_dict.pop('include')
    
    if not isinstance(included_groups, (list, tuple)):
        included_groups = [included_groups]
        
    result = {}
    for group in included_groups:
        if isinstance(group, dict):
            result.update(group)
        elif isinstance(group, str):
            # 假设group是一个文件路径或组名,需要从其他地方加载
            included_dict = self._load_group(group)
            result.update(included_dict)
            
    # 合并include的内容和原始内容
    result.update(parser_dict)
    
    return result