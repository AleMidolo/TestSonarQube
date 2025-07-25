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
            # 假设从某处加载group定义
            group_dict = self._load_group(group)
            result.update(group_dict)
            
    result.update(parser_dict)
    return result