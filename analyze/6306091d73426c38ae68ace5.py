def _include_groups(self, parser_dict):
    """
    解析规范文件中的 include dict 指令。
    """
    if 'include' not in parser_dict:
        return
    
    includes = parser_dict['include']
    for include in includes:
        if isinstance(include, dict):
            self._include_groups(include)
        else:
            self._process_include(include)