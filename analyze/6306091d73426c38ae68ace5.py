def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if not isinstance(parser_dict, dict):
        return parser_dict
        
    if 'include' not in parser_dict:
        return parser_dict
        
    includes = parser_dict.pop('include')
    if not isinstance(includes, list):
        includes = [includes]
        
    result = {}
    for include in includes:
        if isinstance(include, dict):
            result.update(include)
        elif isinstance(include, str):
            # 假设include字符串是一个文件路径
            with open(include, 'r') as f:
                included_dict = self._parse_file(f)
                result.update(included_dict)
                
    result.update(parser_dict)
    return result